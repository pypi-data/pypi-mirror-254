from inquirer import errors
import re

def int_only(_, current):
    re_integer = "^[0-9]*$"
    if not re.search(re_integer, current):
        raise errors.ValidationError('', 'Invalid project id format. Has to be a number')
    return True

def date_format(_, current):
    # tbd: must be future
    re_YYYY_MM_DD_hh_mm = "[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]"
    if not re.search(re_YYYY_MM_DD_hh_mm, current):
        raise errors.ValidationError('', 'Invalid date format. Has to be YYYY-MM-DD hh:mm')       
    return True

def email_address(_, current):
    re_email_address  = "^\S+@\S+\.\S+$"
    if not re.search(re_email_address, current):
        raise errors.ValidationError('', 'Invalid email address format.')
    return True

def not_empty(_, current):
    if current == "":
         raise errors.ValidationError('', 'Content cannot be empty.')
    return True

def is_url(_, current):
    re_url = "((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*"
    # https://stackoverflow.com/a/48689681/3127170
    if not re.search(re_url, current):
        raise errors.ValidationError('', 'Invalid URL format.')
    return True