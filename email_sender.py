import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_TO = os.getenv("EMAIL_TO")


def send_email(report):
    message = EmailMessage()

    message["Subject"] = "Linux Health Report"
    message["From"] = EMAIL_ADDRESS
    message["To"] = EMAIL_TO

    # Email body
    message.set_content(report)

    # Attach the generated report file
    filename = "reports/health_report.txt"

    with open(filename, "rb") as file:
        message.add_attachment(
            file.read(),
            maintype="text",
            subtype="plain",
            filename="health_report.txt"
        )

    # Send the email
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(message)

    print("Email sent successfully!")