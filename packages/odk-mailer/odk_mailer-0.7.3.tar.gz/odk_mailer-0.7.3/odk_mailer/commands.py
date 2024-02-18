from odk_mailer.lib import * 
from odk_mailer.classes import *
from email.message import EmailMessage
import os
import sys

def create(input_source, input_fields, input_message, input_schedule):
   
    # source
    if not input_source:
        source_data = prompts.prompt_source()
    else: 
        source_data = parser.parse_source(input_source)
    source = Source(source_data)

    # fields
    headers = source.get_headers()
    if not input_fields:
        fields_data = prompts.prompt_fields(headers)
    else: 
        fields_data = parser.parse_fields(input_fields, headers)
    fields = Fields(fields_data)

    # message
    if not input_message:
        message_data = prompts.prompt_message()
    else:
        message_data = parser.parse_message(input_message)
    message = Message(message_data)

    # schedule
    if not input_schedule:
        schedule_data = prompts.prompt_schedule()
    else:
        schedule_data = parser.parse_schedule(input_schedule)
    schedule = Schedule(schedule_data)        

    # mailjob
    mailjob = Mailjob()
    created = mailjob.create(source, fields, message, schedule)
    
    print(f"Created {created}")
    log.write(f"Created {created}")
    
    ###
    # Features
    ###

    # 1. Reminders 
    # tbd: Reminders
    # reminders have two attributes:
    # total_amount, frequency, e.g. 3 times in total, every hour|day|week|custom frequency
    # after first scheduled send

    # reminders will be stored inside .odk-mailer/reminder/hash_[instance_id].json
    # having updated recipients from non-respondents (calculated from base recipients and respondents) 
    # on a per reminder case

    # https://github.com/tertek/zapier-odk-scripts/blob/main/get_non_responding.py
    # reminders require api connection and following inputs
    # form_register = "test_form_register" #name of form that is used for registration, given as api or csv
    # form_follow = "test_form_follow"  # name of form that is used for follow up
    # # if use_form_attachment
    # form_follow_attached = "test_form_follow_attached" # name of form that is used for follow up; 
    # form_attachment = "follow.csv" # name of form attachment attached to form_follow; 
    # # field config
    # field_email_register = "email_register" # name of email field for registration form, given
    # field_email_follow = "email_follow"
    # field_email_follow_attach = "email"

    # 2. Cron Jobs
    # add cron-job via https://pypi.org/project/python-crontab/ and https://stackabuse.com/scheduling-jobs-with-python-crontab/
    # We will can use a single job, that checks every hour if we have pending Mailjobs, running 'odk-mailer evaluate
    # process reminder tasks as follows: 
    # 1. Perform API request to calculate reminder recipients
    # 2. Send Emails based on calculated recipients
    # 3. Summarize progress

    # 3. Recipients Validation
    # Validate recipients and ignore (e.g. filter) invalid emails to proceed
    # code example
    # if not recipients.validate(email_field):
    #     utils.render_table(["id", "email_field", "error"], recipients.invalidEmails)
    #     ignore_invalid_emails = typer.confirm("Invalid emails found. Would you like to continue although you have invalid emails?")
    
    #     if not ignore_invalid_emails:
    #         raise typer.Exit("\nAborted.")

    # with typer.progressbar(self.data) as progress:
    #     for row in progress:
    #         total += 1
    #         email = row[email_field]
    #         try:
    #             if not email:
    #                 raise EmailNotValidError("Email address missing. Check for missing delimiters (',') in your CSV file.")
    #             # Disable DNS checks since this can be blocked for unknown reasons within network.
    #             validate_email(email, check_deliverability=True)
    #         except EmailNotValidError as e:
    #             invalid = [str(total) ,email, str(e)]
    #             invalid_emails.append(invalid)


# Run mailjob depending on state:
# state==0: pending
# state==1: success
# state==2: failure
def run(hash_or_id, dry=False, verbose=False, retry=False)->bool:

    mailjob = Mailjob(hash_or_id)
    mailer = Mailer(dry, verbose)

    state = db.read_meta(hash_or_id)["state"]

    # check if can be sent
    # check scheduel time
    if mailjob.schedule.timestamp> utils.now():
        utils.abort("Mailjob is scheduled for future.")

    # check state
    if state == 1:        
        print("Mailjob was already processed with success.")
    
    if state == 2:        
        print("Mailjob was already processed with failure.")
        # retry?
        confirmed = True if retry else prompts.prompt_confirmRetryRun()["confirmRetryRun"]

        if not confirmed:
            return


    hasErrors, errors = mailer.send(mailjob)

    if not dry:
        if not hasErrors:
            mailjob.updateState(1)
            print(f"Success: Run {mailjob.hash}")
            log.write(f"Success: Run {mailjob.hash}")
            return True

        else: 
            mailjob.updateState(2)
            print(f"Failure: Running {mailjob.hash}")
            log.write(f"Failure: Running {mailjob.hash}", "error")
            print("For more information about errors see '~/.odk-mailer/odk-mailer.log'")
            return False

            # errorsString = ""
            # for idx, error in enumerate(errors):
            #         errorsString = errorsString + idx + ": " +vars(error) + "\n\n"

            # log.write(f"Errors: \n\n{errors}", "error")
            # if verbose:
            #     print(f"Errors:  \n\n{ ','.join(errors) }")


def delete(hash_or_id):

    if not hash_or_id:
        utils.abort("ID is required")
        
    found = db.read_meta(hash_or_id)

    if not found:
        utils.abort("Job not found.")
   
    # tbd: confirm
    
    # deletion from /job/<hash>.json
    path_job = os.path.join(globals.odk_mailer_jobs, found['hash']+'.json')
    if os.path.exists(path_job):
        os.remove(path_job)

    # deletion from meta.json
    jobs_meta_new = list(filter(lambda x: x['hash']!=found['hash'], db.read_meta()))
    db.write_meta(jobs_meta_new)
    
    print("Deleted " + found['hash'])    

def list_jobs():

    jobsMeta = db.read_meta()
    if len(jobsMeta) > 0:
        utils.print_jobs(jobsMeta)

    else: print("There are no mailjobs yet. Create one to see it listed.")

def evaluate(force=False, dry=False, verbose=False, notify=False):

    jobs = db.read_meta()

    evaluated = list(filter(lambda job: job["state"] == 0 and job["scheduled"] <= utils.now(), jobs))
    total = len(evaluated)

    isCronProcess = sys.stdout.isatty() == False

    if not dry:        
        if isCronProcess:
            # https://stackoverflow.com/a/2087031/3127170  
            log.write(f"Evaluate run from cron (HOST: {os.getenv('SMTP_HOST')} PORT: {os.getenv('SMTP_PORT')})")
        else: 
            log.write("Evaluate run manually")

        log.write(f"Run evaluate found {total} mailjobs.")

    # # advanced evaluation: addtionally check if job has reminder times that are smaller/equal to now
    # # if true, add to selected list
    # print("Addiitonally checking if we have any valid reminders")
    # for reminder in job["reminders"]:
    #     if reminder["timestamp"] <= utils.now():
    #         evals.append(job["hash"])
    #         break

    if total > 0:
        print(f"Evaluated {total} mailjobs.")

        confirmed = True if force else prompts.prompt_confirmRun()["confirmRun"]

        if confirmed:
            print(f"Confirmed to run {total} mailjobs.")
            if not dry:
                utils.print_success(f"Confirmed to run {total} mailjobs.")
            for idx, eval in enumerate(evaluated):
                print()
                print(f"Running mailjob #{idx+1} of {total} ({eval['hash']})")
                success = run(eval["hash"], dry, verbose)
                print()

                if not dry and success:
                    utils.print_success(f"Evaluated and run {eval['hash']}")
                    log.write(f"Evaluated and run {eval['hash']}")

                if not dry and success and notify:
                    log.write("Sending notifications")
                    notification.send(eval)

    else:
        print("No mailjobs available to be run.")

def config():
    config = Config()
    config.print()

def test(sender, recipient, host, port, username="", password=""):

    smtp_config = [host, port, username, password]

    subject = "Test Mail"
    message = "This is a test mail. Time: " + str(utils.now())

    email = EmailMessage()
    email['From'] = sender
    email['To'] = recipient
    email['Subject'] = subject
    email.set_content(message, subtype="plain")


    print()
    print(f"Sending test mail from {sender} to: {recipient} via: {host}:{port}")
    if username and password:
        print(f"Authentication will be used.")
    print()

    log.write("Sending Test Mail")
    smtp.send(email, True, smtp_config)

def logs():
    log.read()

def crontab_show():
    cron.show()

def crontab_init():
    cron.init()

def crontab_enable():
    cron.enable()

def crontab_disable():
    cron.disable()

def crontab_clear():
    cron.clear()