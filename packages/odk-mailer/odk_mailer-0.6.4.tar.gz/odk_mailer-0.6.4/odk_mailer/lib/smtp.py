from odk_mailer.lib import log, utils
import smtplib

def send(email, verbose=False, smtp_config=[]):

    if not smtp_config:
        log.write("Fatal Error: Invalid configuration given during smtp.send call.", "error")
        raise Exception("Fatal Error: No Configuration File found.")
    
    smtp_host, smtp_port, smtp_user, smtp_pass = smtp_config       

    try:            
        smtp = smtplib.SMTP(timeout=5)
        if verbose:
        # enable debugging by CLI flag --debug
            smtp.set_debuglevel(2)

        smtp.connect(smtp_host, smtp_port)

        if smtp_user and smtp_pass:
        # if username and password are supplied, smtp.login()            
            smtp.login(smtp_user, smtp_pass)
        
        smtp.send_message(email)
        smtp.quit()

        log.write(f"Successfully sent email to {email['To']}")

        return [ utils.now(), False]
    
    except Exception as error:
        log.write("Failed sending mail to: " + email["To"], error)
        log.write(error, "error")

        return [None, error]