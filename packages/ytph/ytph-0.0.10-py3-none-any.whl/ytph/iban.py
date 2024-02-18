from pydantic import BaseModel, computed_field
from schwifty import IBAN, exceptions


class IbanResponse(BaseModel):
    iban: str
    is_valid: bool
    message: str = ""
    parsed: IBAN | str = ""

    @computed_field
    def bank(self) -> dict:
        return self.parsed.bank if self.parsed else {}

    @computed_field
    def country(self) -> dict:
        return self.parsed.country.__dict__["_fields"] if self.parsed else {}

    @computed_field
    def spec(self) -> dict:
        return self.parsed.spec if self.parsed else {}

    @computed_field
    def formatted(self) -> str:
        return self.parsed.formatted if self.parsed else ""


def validate_iban(iban: str) -> IbanResponse:
    try:
        _iban = IBAN(iban, allow_invalid=False, validate_bban=True)
    except exceptions.SchwiftyException as e:
        return IbanResponse(iban=iban, is_valid=False, message=str(e))
    else:
        return IbanResponse(iban=iban, is_valid=True, parsed=_iban)
