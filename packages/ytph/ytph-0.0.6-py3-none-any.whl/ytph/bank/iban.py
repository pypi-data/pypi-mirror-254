from schwifty import IBAN


def validate_iban(iban: str) -> bool:
    iban = IBAN(iban, allow_invalid=True)
    return iban.is_valid
