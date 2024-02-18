import csv
from types import SimpleNamespace

class Source:
    type: str
    location: str
    project: int    
    hostname: str
    username: str
    password: str

    def __init__(self, data):

        if type(data) is dict:
            self.type = data["type"]

            if self.type == "path":
                self.location = data["location"]
            
            if self.type == "url":
                self.location = data["location"]

            if self.type == "api":
                self.location = data["location"]
                self.project = data["api_proj"]
                self.hostname = data["api_host"]
                self.username = data["api_user"]
                self.password = data["api_pass"]

        if type(data) is SimpleNamespace:
            self.type = data.type
            self.location = data.location

    def get_headers(self):
        if self.type == 'path':        
            with open(self.location, newline='') as f:
                dialect = csv.Sniffer().sniff(f.read(1024))
                f.seek(0)
                reader = csv.DictReader(f, skipinitialspace=True, delimiter=dialect.delimiter)
                headers = reader.fieldnames
            return headers
        
        raise Exception("Source type is not yet implemented" )

    def get_rows(self):
        if self.type == 'path':        
            with open(self.location, newline='') as f:
                dialect = csv.Sniffer().sniff(f.read(1024))
                f.seek(0)
                reader = csv.DictReader(f, skipinitialspace=True, delimiter=dialect.delimiter)
                rows = []
                for row in reader:
                    rows.append(row)

            return rows
        
        raise Exception("Source type is not yet implemented" )
       