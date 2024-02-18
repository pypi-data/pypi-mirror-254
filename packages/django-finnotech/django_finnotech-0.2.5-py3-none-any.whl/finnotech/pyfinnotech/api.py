import logging
from json import JSONDecodeError
from logging import Logger
from uuid import uuid4

from django.core.cache import cache
import requests

from .const import (
    SCOPE_BOOMRANG_SMS_SEND_EXECUTE,
    SCOPE_BOOMRANG_SMS_VERIFY_EXECUTE,
    SCOPE_BOOMRANG_TOKEN_DELETE,
    SCOPE_BOOMRANG_TOKENS_GET,
    SCOPE_BOOMRANG_WAGES_GET,
    NATIONAL_CODE_MOBILE_VERIFICATION_CACHE_KEY,
    POSTAL_CODE_INQUIRY_CACHE_KEY,
    IBAN_INQUIRY_CACHE_KEY,
    DEPOSIT_TO_IBAN_CACHE_KEY,
    BACK_CHEQUES_INQUIRY_CACHE_KEY,
    CACHE_TTL,
    CLIENT_IDENTIFICATION_INQUIRY_CACHE_KEY,
    SCOPE_CREDIT_SMS_BACK_CHEQUES_GET,
    SCOPE_CREDIT_SMS_FACILITY_INQUIRY_GET,
    SCOPE_ECITY_CC_POSTAL_CODE_INQUIRY,
    SCOPE_FACILITY_SHAHKAR_GET,
    URL_MAINNET,
    URL_SANDBOX,
)
from .exceptions import FinnotechException, FinnotechHttpException
from .responses import (
    BackChequesInqury,
    ClientIdentificationInquiry,
    NationalcodeMobileVerification,
    PostalcodeInquiry,
    DepositToIban,
    IbanInquiry,
)
from .token import ClientCredentialToken, Token


class FinnotechApiClient:
    def __init__(
        self,
        client_id,
        client_secret=None,
        client_national_id=None,
        scopes=None,
        is_sandbox=False,
        logger: Logger = None,
        requests_extra_kwargs: dict = None,
        client_credential_token=None,
        client_credential_refresh_token=None,
        authorization_token=None,
        base_url=None,
    ):
        self.server_url = base_url or (
            URL_SANDBOX if is_sandbox is True else URL_MAINNET
        )
        self.logger = logger or logging.getLogger("pyfinnotech")
        self.client_id = client_id
        self.client_secret = client_secret
        self.client_national_id = client_national_id
        self.scopes = scopes or [
            SCOPE_BOOMRANG_SMS_SEND_EXECUTE,
            SCOPE_BOOMRANG_SMS_VERIFY_EXECUTE,
            SCOPE_BOOMRANG_TOKEN_DELETE,
            SCOPE_BOOMRANG_TOKENS_GET,
            SCOPE_CREDIT_SMS_BACK_CHEQUES_GET,
            SCOPE_CREDIT_SMS_FACILITY_INQUIRY_GET,
            SCOPE_ECITY_CC_POSTAL_CODE_INQUIRY,
            SCOPE_FACILITY_SHAHKAR_GET,
            SCOPE_BOOMRANG_WAGES_GET,
        ]
        self.requests_extra_kwargs = requests_extra_kwargs or {}
        self._client_credential_token = None
        if client_credential_token is not None:
            self._client_credential_token = ClientCredentialToken.load(
                raw_token=client_credential_token,
                refresh_token=client_credential_refresh_token,
            )

    @classmethod
    def _generate_track_id(cls):
        return uuid4().__str__()

    @property
    def client_credential(self):
        if (
            self._client_credential_token is not None
            and self._client_credential_token.is_valid is True
        ):
            pass
        else:
            self._client_credential_token = ClientCredentialToken.fetch(self)
        return self._client_credential_token

    def _execute(
        self,
        uri,
        method="get",
        params=None,
        headers=None,
        body=None,
        token: Token = None,
        error_mapper=None,
        no_track_id=False,
    ):
        params = params or dict()
        headers = headers or dict()
        track_id = self._generate_track_id() if no_track_id is False else None
        if track_id is not None:
            params.setdefault("trackId", track_id)
        self.logger.debug(
            f"Requesting"
            f" on {uri} with id:{track_id}"
            f" with parameters: {'.'.join(str(params))}"
        )

        if token is not None:
            headers = {**headers, **token.generate_authorization_header()}

        try:
            response = requests.request(
                method,
                "".join([self.server_url, uri]),
                params=params,
                headers=headers,
                proxies={"socks5": "localhost:2020"},
                json=body,
                **self.requests_extra_kwargs,
            )

            if response.status_code == 403:
                self.logger.info("Trying to refresh token")
                token.refresh(self)

                response = requests.request(
                    method,
                    "".join([self.server_url, uri]),
                    params=params,
                    headers=headers,
                    json=body,
                    **self.requests_extra_kwargs,
                )

            if response.status_code != 200:
                raise FinnotechHttpException(response, self.logger)

            try:
                return response.json()
            except JSONDecodeError as e:
                raise FinnotechHttpException(
                    response=response, logger=self.logger, underlying_exception=e
                )

        except FinnotechHttpException as e:
            raise e

        except Exception as e:
            raise FinnotechException(f"Request error: {str(e)}", logger=self.logger)

    def national_code_mobile_verification(self, national_id, mobile):
        if payload := cache.get(
            NATIONAL_CODE_MOBILE_VERIFICATION_CACHE_KEY
            % {"national_code": national_id, "mobile": mobile}
        ):
            return NationalcodeMobileVerification(payload)

        url = f"/facility/v2/clients/{self.client_id}/shahkar/verify?nationalCode={national_id}&mobile={mobile}"

        payload = self._execute(
            uri=url,
            token=self.client_credential,
        )

        cache.set(
            NATIONAL_CODE_MOBILE_VERIFICATION_CACHE_KEY
            % {"national_code": national_id, "mobile": mobile},
            payload,
            CACHE_TTL,
        )

        return NationalcodeMobileVerification(payload)

    def postal_code_inquiry(self, postal_code):
        if (
            payload := cache.get(
                POSTAL_CODE_INQUIRY_CACHE_KEY % {"postal_code": postal_code}
            )
        ) is not None:
            return PostalcodeInquiry(payload)

        url = f"/ecity/v2/clients/{self.client_id}/postalCode?postalCode={postal_code}"

        payload = self._execute(
            uri=url,
            token=self.client_credential,
        )
        cache.set(
            POSTAL_CODE_INQUIRY_CACHE_KEY % {"postal_code": postal_code},
            payload,
            CACHE_TTL,
        )
        return PostalcodeInquiry(payload)

    def client_identification_inquiry(self, national_code: str, birth_date: str):
        if payload := cache.get(
            CLIENT_IDENTIFICATION_INQUIRY_CACHE_KEY
            % {"national_code": national_code, "birth_date": birth_date}
        ):
            return ClientIdentificationInquiry(payload)

        url = f"/kyc/v2/clients/{self.client_id}/identificationInquiry?nationalCode={national_code}&birthDate={birth_date}"

        payload = self._execute(
            uri=url,
            token=self.client_credential,
        )

        cache.set(
            CLIENT_IDENTIFICATION_INQUIRY_CACHE_KEY
            % {"national_code": national_code, "birth_date": birth_date},
            payload,
            CACHE_TTL,
        )
        return ClientIdentificationInquiry(payload)

    def iban_inquiry(self, iban):
        if payload := cache.get(IBAN_INQUIRY_CACHE_KEY % {"iban": iban}):
            return IbanInquiry(payload)

        url = f"/oak/v2/clients/{self.client_id}/ibanInquiry?&iban={iban}"

        payload = self._execute(
            uri=url,
            token=self.client_credential,
        )

        cache.set(IBAN_INQUIRY_CACHE_KEY % {"iban": iban}, payload, CACHE_TTL)
        return IbanInquiry(payload)

    def deposit_to_iban(self, bank_code: str, deposit: str):
        if payload := cache.get(
            DEPOSIT_TO_IBAN_CACHE_KEY % {"deposit": deposit, "bank_code": bank_code}
        ):
            return DepositToIban(payload)

        url = f"/facility/v2/clients/{self.client_id}/depositToIban?deposit={deposit}&bankCode={bank_code}"

        payload = self._execute(
            uri=url,
            token=self.client_credential,
        )
        cache.set(
            DEPOSIT_TO_IBAN_CACHE_KEY % {"deposit": deposit, "bank_code": bank_code},
            payload,
            CACHE_TTL,
        )
        return DepositToIban(payload)

    def back_cheques_inquiry(self, national_id: str, token: str):
        if payload := cache.get(
            BACK_CHEQUES_INQUIRY_CACHE_KEY % {"national_code": national_id}
        ):
            return BackChequesInqury(payload)

        url = f"/credit/v2/clients/{self.client_id}/users/{national_id}/sms/backCheques"

        payload = self._execute(uri=url, token=token)
        cache.set(
            BACK_CHEQUES_INQUIRY_CACHE_KEY % {"national_code": national_id},
            payload,
            CACHE_TTL,
        )
        return BackChequesInqury(payload)
