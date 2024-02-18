from types import SimpleNamespace
class Fields:
    email: str
    data: []

    def __init__(self, data):

        if type(data) is dict:           
            self.email = data["email"]
            if "data" in data:
                self.data = data["data"]
            else:
                self.data = []

        if type(data) is SimpleNamespace:
            self.email = data.email
            self.data  = data.data