from odk_mailer.lib import utils
from types import SimpleNamespace

class Message:
    sender: str
    subject: str
    source: str
    location: str
    format: str
    content: str

    def __init__(self, data) -> None:

        if type(data) is dict:
            self.sender = data["sender"]
            self.subject = data["subject"]
            self.source = data["source"]
            self.format = data["type"]
            self.location = data["location"]            
            self.setContent()

        if type(data) is SimpleNamespace:
            self.sender = data.sender
            self.subject = data.subject
            self.source = data.source
            self.format = data.format
            
            # backwards compatibility
            try:
                self.location = data.location
                self.setContent()
            except:
                self.content = data.content

    def setContent(self):
        if self.source == "stdin":
                self.content = self.location

        if self.source == "path":            
            with open(self.location) as f:
                data_string = f.read()
                # base64_string = utils.base64_encode_str(data_string)
                # self.content = base64_string
                self.content = data_string

        if self.source == "url":
            #tbd: read from url and store as base64
            self.content = self.location