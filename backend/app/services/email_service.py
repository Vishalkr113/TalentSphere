import logging
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from app.core.config import settings

logger = logging.getLogger(__name__)

SMTP_HOST = settings.SMTP_HOST
SMTP_PORT = int(settings.SMTP_PORT)
SMTP_EMAIL = settings.SMTP_EMAIL
SMTP_PASSWORD = settings.SMTP_PASSWORD
SMTP_FROM = settings.SMTP_FROM


def send_otp_email(recipient_email: str, otp: str) -> bool:

    print("========== OTP DEBUG ==========")
    print("Sending OTP To:", recipient_email)

    """
    Sends OTP email to the specified recipient.

    Returns:
        True  -> Email sent successfully
        False -> Failed to send email
    """

    try:
        message = MIMEMultipart("alternative")
        message["Subject"] = "Verify Your Email - TalentSphere"
        message["From"] = SMTP_FROM
        message["To"] = recipient_email

        html = f"""
        <html>
        <body style="font-family: Arial, sans-serif;">
            <h2>TalentSphere Email Verification</h2>

            <p>Your OTP is:</p>

            <h1 style="letter-spacing:6px;color:#2563eb;">
                {otp}
            </h1>

            <p>This OTP is valid for <strong>10 minutes</strong>.</p>

            <p>If you didn't request this email, you can safely ignore it.</p>
        </body>
        </html>
        """

        message.attach(MIMEText(html, "html"))

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(
            SMTP_HOST,
            SMTP_PORT,
            context=context,
            timeout=30,
        ) as server:

            server.login(
                SMTP_EMAIL,
                SMTP_PASSWORD,
            )

            server.sendmail(
                SMTP_FROM,
                recipient_email,
                message.as_string(),
            )

        logger.info("OTP email sent successfully to %s", recipient_email)
        return True

    except Exception:
        logger.exception("Failed to send OTP email to %s", recipient_email)
        return False