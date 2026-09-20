import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from utils.config import Config
from utils.logger import setup_logger

logger = setup_logger("emailer")

class EmailDelivery:
    def __init__(self):
        self.config = Config()

    def send_email(self, subject, content):
        if not all([self.config.EMAIL_SENDER, self.config.EMAIL_PASSWORD, self.config.EMAIL_RECEIVER]):
            logger.warning("Email settings not fully configured in .env. Skipping email.")
            return False

        message = MIMEMultipart()
        message["From"] = self.config.EMAIL_SENDER
        message["To"] = self.config.EMAIL_RECEIVER
        message["Subject"] = subject
        
        message.attach(MIMEText(content, "plain"))

        try:
            with smtplib.SMTP(self.config.SMTP_SERVER, self.config.SMTP_PORT) as server:
                server.starttls()
                server.login(self.config.EMAIL_SENDER, self.config.EMAIL_PASSWORD)
                server.send_message(message)
                logger.info("Email sent successfully.")
                return True
        except Exception as e:
            logger.error(f"Failed to send email: {e}")
            return False
