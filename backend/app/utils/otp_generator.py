import secrets
import string


OTP_LENGTH = 6


def generate_otp() -> str:
    """
    Generate a secure 6-digit numeric OTP.
    """
    digits = string.digits
    return "".join(
        secrets.choice(digits)
        for _ in range(OTP_LENGTH)
    )