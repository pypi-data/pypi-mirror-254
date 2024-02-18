from odk_mailer.lib import utils,smtp
from odk_mailer.classes import Config
from email.message import EmailMessage
import socket
import os
import time

def send(eval):

    NOTIFY_TO = os.getenv('NOTIFY_TO')
    NOTIFY_FROM = os.getenv('NOTIFY_FROM')

    if not NOTIFY_FROM or not NOTIFY_TO:
        return

    smtp_config = Config(smtpRequired=True).get_smpt_config()

    subject = f"[ODK-Mailer] Successful run for {eval['hash'][:10]}"

    message =   f"ODK-Mailer has successfully completed a mailjob:\n\n"\
                f"Job ID: {eval['hash']}\n"\
                f"Note: {eval['note']}\n"\
                f"Recipients: {eval['recipients']}\n"\
                f"Created: {utils.ts_to_str(eval['created'])}\n"\
                f"Scheduled: {utils.ts_to_str(eval['scheduled'])}\n"\
                f"Sent: {utils.ts_to_str(utils.now())}\n\n"\
                f"Host: {socket.gethostname()} ({utils.get_ip()})\n"\
                f"Timezone: {time.localtime().tm_zone})\n\n"\
                "You are getting this email, because your address has been added to the ODK-Mailer notification list.\n"\
                "If you would like to stop receiving these messages, demand removal of your address from NOTIFY_TO environment variable."

    email = EmailMessage()
    email['From'] = NOTIFY_FROM
    email['To'] = NOTIFY_TO
    email['Subject'] = subject
    email.set_content(message, subtype="plain")

    smtp.send(email, False, smtp_config)