from twilio.rest import Client
import smtplib

TWILIO_SID = "AC932a32bf1f342adb539eb5b491490e2b"
TWILIO_AUTH_TOKEN = "74a5c13cd56460b8b011d6acf2cf437c"
TWILIO_VIRTUAL_NUMBER = "+12058469440"
TWILIO_VERIFIED_NUMBER = "+919987717561"
MY_EMAIL = "pythonpractice291202@gmail.com"
MY_PASSWORD = "plmqaz123098TG"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=MY_EMAIL,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )

    """def send_mails(self, emails, message, google_flight_link):
        with smtplib.SMTP('smtp.gmail.com) as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        for email in emails:
            connection.sendmail(
                from_addr=
        """