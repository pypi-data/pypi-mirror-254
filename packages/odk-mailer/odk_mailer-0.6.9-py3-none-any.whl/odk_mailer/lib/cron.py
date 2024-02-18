from odk_mailer.lib import prompts
from crontab import CronTab
import os
import shutil

cron = CronTab(user=True)
CRON_COMMENT = 'odk-mailer-cron'

def init():

    job = find()

    if job and job.is_valid():
        print("Found valid cron job:")
        show()
        confirmed = prompts.prompt_confirmCronReInit()["confirmCronReInit"]

        if confirmed:
            clear()
            create()

    elif job and not job.is_valid():
         print("Found invalid cron job. Clearing and recreating..")
         clear()
         create()
    else:
        create()

def find():

    iter = cron.find_comment(CRON_COMMENT)
    for job in iter:
        return job
    
    return None

def show():

    iter = cron.find_comment(CRON_COMMENT)
    for job in iter:
        print(job)

        
def create():

    # explicit odk-mailer path
    WHICH_ODK = shutil.which("odk-mailer")

    # Passing environment variables to cron seems problematic when working in different environemnts,
    # this needs to be improved for the future
    # for now we will simply pass the explictly inline
    # https://www.baeldung.com/linux/load-env-variables-in-cron-job

    ENV = 'SMTP_HOST='+(os.getenv('SMTP_HOST') or "")\
                +' SMTP_PORT='+ (os.getenv('SMTP_PORT') or "")\
                +' SMTP_USER='+ (os.getenv('SMTP_USER') or "")\
                +' SMTP_PASS='+ (os.getenv('SMTP_PASS') or "")\
                +' ODK_HOST='+ (os.getenv('ODK_HOST') or "")\
                +' NOTIFY_TO='+ (os.getenv('NOTIFY_TO') or "")\
                +' NOTIFY_FROM='+ (os.getenv('NOTIFY_FROM') or "")
    
    CRON_COMMAND = ENV + ' bash -c "' +  WHICH_ODK + ' jobs evaluate --force --notify"'
    
    # alternatives not working:
    # alternative 1: pass /etc/profile to BASH_ENV
    # CRON_COMMAND = 'BASH_ENV=/etc/profile bash -c "' +  WHICH_ODK + ' jobs evaluate --force"'

    # alternative 2: define cron environment
    # cron.env['SHELL'] = '/bin/bash'
    # CRON_COMMAND = WHICH_ODK + ' jobs evaluate --force'
       
    job = cron.new(        
        command = CRON_COMMAND,
        comment= CRON_COMMENT
        )
    
    # Set to every 15 Minutes
    # testing every minute
    job.minute.every(1)    
    cron.write()
    print("Created cron job")
    show()

def clear():
    cron.remove_all(comment=CRON_COMMENT)
    print("Removed cron job")

def enable():
    job = find()
    if job:
        job.enable()

def disable():
    job = find()
    if job:
        job.enable(False)
