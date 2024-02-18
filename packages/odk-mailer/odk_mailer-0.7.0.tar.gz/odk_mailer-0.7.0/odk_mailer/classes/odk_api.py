import requests
import csv
from io import StringIO

class ODKClient:
    def __init__(self):
        self.base = "" #e.g. https://odk-central-testing.swisstph.ch/v1/projects
        self.project = "" #eg, 47
        self.token = "" #eg, base64 encoded from user:pass string
        self.form = "" # e.g. form-1
        self.file = "" # e,g, form-1-attachement.csv

    def auth(self):
        
        url = self.base + "/" + self.project

        payload = {}
        headers = {
        'Authorization': 'Basic '+self.token
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

    def submissions_data(self):
        
        url = self.base + "/" + self.project + "/forms" + "/" + self.form + "/submissions.csv"

        payload = {}
        headers = {
        'Authorization': 'Basic '+self.token
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

    def form_attachment(self):

        url = self.base + "/" + self.project + "/forms" + "/" + self.form + "/attachments" +"/" + self.file

        payload = {}
        headers = {
        'Authorization': 'Basic ' + self.token
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

        # convert string to file object
        f = StringIO(response.text)

        cr = csv.DictReader(f)

        emails = []

        for row in cr:
            emails.append(row["label"])

        print(emails)

        output = {'registered_emails': emails}

        #print(response.text)
