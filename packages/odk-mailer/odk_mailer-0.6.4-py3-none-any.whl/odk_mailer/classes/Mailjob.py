from odk_mailer.classes.Source import Source
from odk_mailer.classes.Fields import Fields
from odk_mailer.classes.Message import Message
from odk_mailer.classes.Schedule import Schedule
from odk_mailer.classes.JobMeta import JobMeta


from odk_mailer.lib import globals, utils,db
import os
import json
import sys
from json import JSONEncoder
import hashlib
from types import SimpleNamespace

# return unformatted string instead of raising error
# when key is missing within dictionary
# https://stackoverflow.com/a/17215533/3127170
class SafeDict(dict):
    def __missing__(self, key):
        return '{' + key + '}' 

# custom encoder for JSONEncoder
# https://pynative.com/python-convert-json-data-into-custom-python-object/
class MailjobEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
    
class Mailjob:
    source: Source
    fields: Fields
    message: Message
    schedule: Schedule
    created: int

    hash: str
    json: str

    def __init__(self, hash_or_id = "") -> None:

        if hash_or_id != "":
            self.hash = hash_or_id
            self.hash = self.find()
            self.load()

    def find(self):
        if not self.hash:
            raise Exception("Invalid operation. Hash required")
        
        jobs_meta = db.read_meta()
        found = next((obj for obj in jobs_meta if obj["hash"].startswith(self.hash)), None)

        if not found:
            utils.abort("Job not found.")        

        return found["hash"]

    def load(self):

        with open(os.path.join(globals.odk_mailer_jobs, self.hash+'.json'), 'r', encoding='utf-8') as f:
            job = json.load(f, object_hook=lambda d: SimpleNamespace(**d))
        
        # this may be optimized...
        self.source = Source(job.source)
        self.field = Fields(job.fields)
        self.message = Message(job.message)
        self.schedule = Schedule(job.schedule)
        self.recipients = job.recipients

        self.created = job.created

    def create(
        self, 
        source: Source, 
        fields: Fields, 
        message: Message, 
        schedule: Schedule
        ) -> str:

        self.source = source
        self.fields = fields
        self.message = message
        self.schedule = schedule
        self.created = utils.now()

        self.setRecipients()
        self.json = json.dumps(vars(self), ensure_ascii=True, indent=4, cls=MailjobEncoder)
        self.hash = hashlib.sha256(self.json.encode()).hexdigest()

        self.save()
        return self.hash

    def setRecipients(self):
        recipients = []

        for row in self.source.get_rows():   
            f_row = {k: row[k] for k in self.fields.data + [self.fields.email] }
            recipients.append(f_row)
        self.recipients = recipients

    def save(self)->None:
        # add to jobs
        path_to_job = os.path.join(globals.odk_mailer_jobs, self.hash+'.json')
        with open(path_to_job, 'w', encoding='utf-8') as f:
            f.write(self.json)

        # add to meta
        jobs_meta = db.read_meta()
        jobs_meta.append(JobMeta(self).__dict__)
        db.write_meta(jobs_meta)
    
    #tbd: def delete(self):

    def updateState(self, state):

        if not state in [0,1,2]:
            raise Exception("Invalid state")

        def mapNewMeta(job_meta):
            if job_meta["hash"] == self.hash:
                 job_meta["state"] = state

            return job_meta

        jobs_meta = list(map(mapNewMeta, db.read_meta()))
        db.write_meta(jobs_meta)




        

