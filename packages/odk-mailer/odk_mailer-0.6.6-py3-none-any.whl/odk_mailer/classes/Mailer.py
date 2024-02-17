from odk_mailer.classes import Mailjob
from odk_mailer.classes.Config import Config
from odk_mailer.lib import utils, smtp, log
from rich.progress import track
from email.message import EmailMessage
import time
import sys


class Mailer:
    mailjob: Mailjob
    verbose: bool
    dry: bool

    def __init__(self, dry=False, verbose=False) -> None:
        self.dry = dry
        self.verbose = verbose

    def send(self, mailjob: Mailjob):

        self.mailjob = mailjob
        success = []
        errors = []

        if not self.dry:
            log.write(f"Running mailjob {self.mailjob.hash}")

        if self.verbose:           
            print()
            print(f"Running mailjob {self.mailjob.hash}")            
            if self.dry:
                print("Dry Run enabled -no Emails will be sent.")
            print()

        # Decode base64 if needed (currently disabled for issues with ISO decoding of ä characters)
        if self.mailjob.message.source == "stdin":
            text = self.mailjob.message.content
        if self.mailjob.message.source in ["path", "url"]:
            #text = utils.base64_decode_str(self.mailjob.message.content)
            text = self.mailjob.message.content

        # Retrieve SMTP Config with required parameters
        smtp_config = Config(smtpRequired=True).get_smpt_config()
        total_recipients= len(self.mailjob.recipients)

        if self.dry:
            print()
            print("Message Summary")
            print("-----------------------------------------")
            print(f"sender: {self.mailjob.message.sender}")
            print(f"subject: {self.mailjob.message.subject}")
            print(f"source: {self.mailjob.message.source}")
            print(f"format: {self.mailjob.message.format}")
            print(f"# recipients: {total_recipients}")
            print("-----------------------------------------")
            print()

            for idx, recipient in enumerate(self.mailjob.recipients):
                content = utils.safe_format_map(text, recipient)
                print(f"# {idx+1}|{total_recipients} ({recipient.email})")
                print()
                utils.print_mail(content)

        else:
            total = 0

            if self.verbose:
                print(f"Preparing to send {total_recipients} mails")
            log.write(f"Preparing to send {total_recipients} mails")

            for recipient in track(self.mailjob.recipients, description="Processing.."):

                content = utils.safe_format_map(text, recipient)

                email = EmailMessage()
                email['From'] = self.mailjob.message.sender
                email['To'] = recipient.email
                email['Subject'] = self.mailjob.message.subject
                email.set_content(content, subtype=self.mailjob.message.format)

                log.write(f"#{total} of {total_recipients}: Attempting to send mail to {email['To']}")
                
                if self.verbose:
                    print()
                    print(f"#{total} of {total_recipients}: Attempting to send mail to {email['To']}")

                [sent, error] = smtp.send(email, self.verbose, smtp_config)

                if sent:
                    success.append(sent)
                    if self.verbose:
                        print()
                        print("Successfully sent email to " + email["To"])
                        print()                    

                if error:
                    errors.append(error)
                    if self.verbose:
                        print(error)
                        print("Failed sending mail to: " + email['To'])
                        print()                    

                # Fake processing time
                # time.sleep(0.01)
                total += 1
            
            print(f"Processed {total} mails with {len(success)} success and {len(errors)} failure.")            
            log.write(f"Processed {total} mails with {len(success)} success and {len(errors)} failure.")

        return [ len(errors) > 0, errors]