from pydantic import BaseModel, computed_field
from schwifty import IBAN, exceptions


class IbanResponse(BaseModel):
    iban: str
    is_valid: bool
    message: str = ""
    parsed: IBAN | str = ""

    @computed_field
    def account(self) -> dict:
        if self.parsed:
            return {
                "bban": self.parsed.bban.__str__(),
                "checksum_digits": self.parsed.checksum_digits,
                "account_code": self.parsed.account_code,
                "account_type": self.parsed.account_type,
                "in_sepa_zone": self.parsed.in_sepa_zone,
                "national_checksum_digits": self.parsed.national_checksum_digits,
                "numeric": self.parsed.numeric,
                "formatted": self.parsed.formatted,
            }
        return {}

    @computed_field
    def bank(self) -> dict:
        return self.parsed.bank if self.parsed else {}

    @computed_field
    def country(self) -> dict:
        return self.parsed.country.__dict__["_fields"] if self.parsed else {}

    @computed_field
    def spec(self) -> dict:
        return self.parsed.spec if self.parsed else {}


def validate_iban(iban: str) -> IbanResponse:
    try:
        _iban = IBAN(iban, allow_invalid=False, validate_bban=True)
    except exceptions.SchwiftyException as e:
        return IbanResponse(iban=iban, is_valid=False, message=str(e))
    else:
        return IbanResponse(iban=_iban.compact, is_valid=True, parsed=_iban)
