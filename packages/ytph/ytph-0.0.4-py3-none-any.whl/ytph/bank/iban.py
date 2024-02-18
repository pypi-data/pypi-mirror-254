from schwifty import IBAN


def validate_iban(iban):
    iban = IBAN(iban, allow_invalid=True)
    return iban.is_valid
