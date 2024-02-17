from odk_mailer.lib import utils, log
import os

class Config():
    odk_host: str
    smtp_host: str
    smtp_port: str
    smtp_user: str
    smtp_pass: str
    
    def __init__(self, smtpRequired:bool=False, odkRequired:bool=False):
        
        # loads environment variables from .env file

        ODK_HOST = os.getenv('ODK_HOST')

        SMTP_HOST = os.getenv('SMTP_HOST')
        SMPT_PORT = os.getenv('SMTP_PORT')
        SMPT_USER = os.getenv('SMPT_USER')
        SMPT_PASS = os.getenv('SMPT_PASS')

        if smtpRequired:
            if not SMTP_HOST or not SMPT_PORT:
                log.write("Config Error: SMTP_HOST and SMPT_PORT are required configuration for sending emails.", "error")
                utils.abort("Config Error: SMTP_HOST and SMPT_PORT are required configuration for sending emails.")

        if odkRequired and not ODK_HOST:
            log.write("Config Error: ODK_Host is required configuration for accessing ODK API.", "error")
            utils.abort("Config Error: ODK_Host is required configuration for accessing ODK API.")

        self.smtp_host = SMTP_HOST
        self.smtp_port = SMPT_PORT
        self.smtp_user = SMPT_USER
        self.smtp_pass = SMPT_PASS

        self.odk_host = ODK_HOST     

    def get_smpt_config(self):
        return [self.smtp_host, self.smtp_port, self.smtp_user, self.smtp_pass]
        
    def print(self):

        print()
        print("Your current configuration is: ")    
        for key,value in vars(self).items():
            print(f"{key.upper()}: {value}")
        print()
        print("To change your configuration please setup/edit environment variables or .env file!")