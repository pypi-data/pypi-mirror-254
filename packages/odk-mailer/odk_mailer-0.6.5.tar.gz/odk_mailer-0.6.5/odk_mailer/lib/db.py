import json
from odk_mailer.lib import globals

def read_meta(hash_or_id: str = ''):

    with open(globals.odk_mailer_meta, "r") as f:
        jobs_meta =json.load(f)

        # return all as list
        if not hash_or_id:
            return jobs_meta
        
        # return single with
        job_meta = next((obj for obj in jobs_meta if obj["hash"].startswith(hash_or_id)), None)
    
        return job_meta

def write_meta(jobs_meta_new):
     
     with open(globals.odk_mailer_meta, "w") as f:
         f.write(json.dumps(jobs_meta_new))
    