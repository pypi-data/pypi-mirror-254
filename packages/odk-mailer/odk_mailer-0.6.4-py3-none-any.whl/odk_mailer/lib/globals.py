import os

odk_mailer_base = os.path.join(os.getenv("HOME"), ".odk-mailer")
odk_mailer_meta = os.path.join(odk_mailer_base, "meta.json")
odk_mailer_jobs = os.path.join(odk_mailer_base, "jobs")