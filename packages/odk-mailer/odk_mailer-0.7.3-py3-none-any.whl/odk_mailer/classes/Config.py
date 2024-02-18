from odk_mailer.lib import utils, log
import os

class Config():
    smtp_host: str
    smtp_port: str
    smtp_user: str
    smtp_pass: str
    odk_host: str
    cron_frequency: str
    notify_to: str
    notify_from: str
    
    def __init__(self, smtpRequired:bool=False, odkRequired:bool=False):
        
        # loads environment variables from .env file

        SMTP_HOST = os.getenv('SMTP_HOST')
        SMTP_PORT = os.getenv('SMTP_PORT')
        SMTP_USER = os.getenv('SMTP_USER')
        SMTP_PASS = os.getenv('SMTP_PASS')

        ODK_HOST = os.getenv('ODK_HOST')

        CRON_FREQUENCY = os.getenv('CRON_FREQUENCY')

        NOTIFY_TO = os.getenv('NOTIFY_TO')
        NOTIFY_FROM = os.getenv('NOTIFY_FROM')

        if smtpRequired:
            if not SMTP_HOST or not SMTP_PORT:
                log.write("Config Error: SMTP_HOST and SMPT_PORT are required configuration for sending emails.", "error")
                utils.abort("Config Error: SMTP_HOST and SMPT_PORT are required configuration for sending emails.")

        if odkRequired and not ODK_HOST:
            log.write("Config Error: ODK_Host is required configuration for accessing ODK API.", "error")
            utils.abort("Config Error: ODK_Host is required configuration for accessing ODK API.")

        self.smtp_host = SMTP_HOST
        self.smtp_port = SMTP_PORT
        self.smtp_user = SMTP_USER
        self.smtp_pass = SMTP_PASS

        self.odk_host = ODK_HOST

        self.cron_frequency = CRON_FREQUENCY

        self.notify_to = NOTIFY_TO
        self.notify_from = NOTIFY_FROM

    def get_smpt_config(self):
        return [self.smtp_host, self.smtp_port, self.smtp_user, self.smtp_pass]
        
    def print(self):

        print()
        print("Your current configuration is: ")    
        for key,value in vars(self).items():
            print(f"{key.upper()}: {value}")
        print()
        print("To change your configuration please setup/edit environment variables!")