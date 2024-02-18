from email_validator import validate_email as _validate_email
from email_validator import EmailNotValidError


def validate_email(email: str) -> bool:
    try:
        _ = _validate_email(email, check_deliverability=False)
    except EmailNotValidError:
        return False
    return True
