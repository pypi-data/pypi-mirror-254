from crontab import CronTab
import os
import shutil

cron = CronTab(user=True)
CRON_COMMENT = 'odk-mailer-cron'

def setup():

    job = find()

    if job and job.is_valid():
        #print("Found valid Cron Job.")
        pass
    else:
        clear()
        create()

def find():

    jobExists = False

    genCron = cron.find_comment(CRON_COMMENT)
    for job in genCron:
        jobExists = True

    if jobExists:
        return job

    return None
        
def create():    
    ENV_VARS = 'SMTP_HOST='+(os.getenv('SMTP_HOST') or "") +' SMTP_PORT=' + (os.getenv('SMTP_PORT') or "") + ' SMTP_USER='+ (os.getenv('SMTP_USER') or "") + ' SMTP_PASS='+ (os.getenv('SMTP_PASS') or "") + ' ODK_HOST=' + (os.getenv('ODK_HOST') or "")  #tbd add other or load them dynamically: https://www.baeldung.com/linux/load-env-variables-in-cron-job
    WHICH_ODK = shutil.which("odk-mailer")
    # CRON_COMMAND = 'BASH_ENV=/etc/profile bash -c "' +  WHICH_ODK + ' jobs evaluate --force"' # 2>&1 | logger -t mycmd  https://askubuntu.com/a/967798
    CRON_COMMAND = ENV_VARS + ' bash -c "' +  WHICH_ODK + ' jobs evaluate --force"' # 2>&1 | logger -t mycmd  https://askubuntu.com/a/967798    

    job = cron.new(        
        command = CRON_COMMAND,
        comment= CRON_COMMENT
        )
    
    # Set to every 15 Minutes
    # testing every minute
    job.minute.every(1)
    
    cron.write()
    print("Created Cron Job.")

def clear():
    cron.remove_all(comment=CRON_COMMENT)
    print("Removed Cron Job.")

def enable():
    job = find()
    if job:
        job.enable()

def disable():
    job = find()
    if job:
        job.enable(False)