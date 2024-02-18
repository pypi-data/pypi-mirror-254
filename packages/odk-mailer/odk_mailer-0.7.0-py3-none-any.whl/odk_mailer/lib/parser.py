from odk_mailer.lib import utils, validators
import os

def parse_source(input):

    source_list = input.split("::", 6)
    source_count = len(source_list)
    
    # --source=file::tests/data/valid.csv
    # --source=url::https://some.url.tld/file.csv
    if source_count == 2:

        type, location = source_list

        if type not in ["path", "url"]:
            utils.abort("Invalid source type, expected 'path' or 'url.")

        if type == "path":
            ext = os.path.splitext(location)[-1].lower()
            # invalid file extension
            if not ext == ".csv":
                utils.abort("Invalid file extension, expected '.csv'")
            # invalid file path
            if not os.path.isfile(location):
                utils.abort("Invalid file path, expected existing file")

            return {
                'type': type,
                'location': location
            }
                    
        if type == "url":
            utils.abort("URL not yet supported!")

            return {
                'type': type,
                'location': location
            }            

    if source_count == 6:
        utils.abort("API not yet supported!")

        # type, form, project, host, user, pass = source_list
        # check API connection & credentials
        # promptAPIcredentials() // host, user, pass, project
        # checkAPIconnection()  // auth endpoint

        # return {
        #     'type': type,
        #     'location': form,
        #     'api_proj': project,
        #     'api_host': host,
        #     'api_user': user,
        #     'api_pass': pass
        # }        

    else:
        utils.abort("Invalid file/api source string")


def parse_fields(input, headers):

    fields_list = input.split("::", 2)
    fields_count = len(fields_list)

    if not fields_count in [1,2]:        
        utils.abort("Invalid email/data fields string")
    
    email = fields_list[0]

    if email not in headers:
        utils.abort(f"Invalid email field '{email}'.")

    if fields_count == 1:
        return {
            'email': email
        }
    
    if fields_count == 2:
        data = fields_list[1].split(",") 
        for field in data:
            if not field in filter(lambda x: x != email, headers):
                utils.abort(f"Invalid data field '{field}'")
    
        return {
            'email': email,
            'data': data
        }
    
def parse_message(input):
    message_list = input.split("::", 5)
    message_count = len(message_list)

    if not message_count == 5:
        utils.abort("Define message as \[sender:str]::\[subject:str]::\[source:'stdin'|'path'|'url']::\[location:str]::\[type:'plain'|'html']")

    sender, subject, source, location, type = message_list

    if not validators.email_address("", sender):        
        raise utils.abort("Invalid message sender. Use valid email address.")   
    
    if source not in ["stdin", "path", "url"]:
        raise utils.abort("Invalid message source. Use either 'stdin' or 'path or 'url.")
    
    if type not in ["plain", "html"]:
        raise utils.abort("Invalid message type. Use either 'plain' or 'html'.")    

    if source == "path":
        if not os.path.isfile(location):
            utils.abort("Invalid file path, expected existing file")        
    
    return {
        'sender': sender,
        'subject': subject,
        'source': source,
        'location': location,
        'type': type
    }

def parse_schedule(input):    
    if input == "now":
        now = True
        datetime = None
    else: 
        now = False
        datetime = input

    return {
        'now': now,
        'datetime': datetime
    }