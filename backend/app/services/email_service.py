import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from app.core.config import settings


SMTP_HOST = settings.SMTP_HOST
SMTP_PORT = int(settings.SMTP_PORT)
SMTP_EMAIL = settings.SMTP_EMAIL
SMTP_PASSWORD = settings.SMTP_PASSWORD
SMTP_FROM = settings.SMTP_FROM


def send_otp_email(recipient_email: str, otp: str) -> bool:
    try:
        message = MIMEMultipart("alternative")
        message["Subject"] = "Verify Your Email - TalentSphere"
        message["From"] = SMTP_FROM
        message["To"] = recipient_email

        html = f"""
        <html>
        <body style="font-family:Arial,sans-serif;">
            <h2>TalentSphere Email Verification</h2>

            <p>Your OTP is:</p>

            <h1 style="letter-spacing:6px;color:#2563eb;">
                {otp}
            </h1>

            <p>This OTP is valid for 10 minutes.</p>

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

        print("=" * 60)
        print("EMAIL SENT SUCCESSFULLY")
        print("=" * 60)

        return True

    except Exception as e:
        print("=" * 60)
        print("EMAIL SENDING FAILED")
        print(type(e))
        print(repr(e))
        print("=" * 60)
        return False