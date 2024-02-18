import inquirer
from odk_mailer.lib import validators

def prompt_source():
    questions = [
        inquirer.List('type', 
                    message="Select source type:",
                    choices= [
                        ("File from path", "path"),
                        ("File from url", "url"),
                        ("ODK API", "api")
                    ],                      
                    carousel=True
        ),
        inquirer.Path('location',
                    message="Input local path to CSV file",
                    path_type=inquirer.Path.FILE,
                    exists=True,
                    normalize_to_absolute_path=True,
                    ignore=lambda x: x["type"] != "path"
        ),
        inquirer.Text('location',
                    message="Input URL to CSV file",
                    ignore=lambda x: x["type"] != "url",
                    validate=validators.is_url
        ),        
        inquirer.Text('location',
                    message="Input form/attachment name",                      
                    ignore=lambda x: x["type"] != "api"
                    #tbd: add regex valdation
        ),
        inquirer.Text('api_proj',
                    message="Input project id",
                    validate= validators.int_only,
                    ignore=lambda x: x["type"] != "api"
        ),
        inquirer.Text('api_host',
                    message="Input ODK host url",
                    ignore=lambda x: x["type"] != "api",
                    # tbd validate url, https
        ),
        inquirer.Text('api_user',
                    message="Input ODK username",
                    ignore=lambda x: x["type"] != "api"
        ),
        inquirer.Password('api_pass',
                    message="Input ODK password",
                    ignore=lambda x: x["type"] != "api"
        )
    ]
    return inquirer.prompt(questions, raise_keyboard_interrupt=True)

def prompt_fields(headers=[]):
    questions = [
        inquirer.List('email',
                    message="Select email field",
                    choices=headers,
                    default='email' if 'email' in headers else "",
                    carousel=True
        ),
        inquirer.Checkbox("data", 
                    message="Select data field(s)",
                    choices= lambda x: filter(lambda y: y != x["email"], headers)
        )        
    ]
    return inquirer.prompt(questions, raise_keyboard_interrupt=True)

def prompt_message():
    questions = [
        inquirer.Text('sender',
                    message="Input message sender",
                    default="odk-mailer@freesmtpservers.com",
                    validate=validators.email_address                      
        ),
        inquirer.Text('subject',
                    message="Input message subject",
                    default="ODK-Mailer: New Email"                    
        ),
        inquirer.List('source', 
                    message="Select message source:",
                    choices= [
                        ("Text from stdin", "stdin"),
                        ("File from path", "path"),
                        ("File from url", "url")
                    ],                      
                    carousel=True
        ),        
        inquirer.Text('location',
                    message="Input string",
                    ignore=lambda x: x["source"] != "stdin",
                    validate= validators.not_empty
        ),     
        inquirer.Path('location',
                    message="Input file path",
                    path_type=inquirer.Path.FILE,
                    exists=True,
                    normalize_to_absolute_path=True,
                    ignore=lambda x: x["source"] != "path"
        ),
        inquirer.Text('location',
                    message="Input file url",
                    ignore=lambda x: x["source"] != "url",
                    validate= validators.is_url
        ),        
        inquirer.List('type', 
                    message="Select message type:",
                    choices= [
                        ("Plain", "plain"),
                        ("HTML", "html")
                    ],                      
                    carousel=True
        ),
    ]
    return inquirer.prompt(questions, raise_keyboard_interrupt=True)

def prompt_schedule():
    questions = [
        inquirer.List('now',
                    message="Send now or schedule a date and time?",
                    choices=[
                        ("Send now",True),
                        ("Schedule", False)
                    ]
        ),
        inquirer.Text('datetime',
                    message="Input date and time",
                    validate= validators.date_format,
                    ignore=lambda x: x["now"] == True

        )
    ]

    return inquirer.prompt(questions, raise_keyboard_interrupt=True)

def prompt_confirmRun():
    questions = [
        inquirer.Confirm('confirmRun',
                         message="Would you like to run evaluated mailjobs?"
        )
    ]

    return inquirer.prompt(questions, raise_keyboard_interrupt=True)

def prompt_confirmCronReInit():
    questions = [
        inquirer.Confirm('confirmCronReInit',
                         message="Would you like to re-initialize crontabs?"
        )
    ]

    return inquirer.prompt(questions, raise_keyboard_interrupt=True)