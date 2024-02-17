from pathlib import Path
from odk_mailer.lib import globals
import typer
import json

def init():

  # create base dir if not exists
  path_base = Path(globals.odk_mailer_base)
  path_base.mkdir(parents=True, exist_ok=True)
  
  # create jobs dir if not exists
  path_job = Path(globals.odk_mailer_jobs)
  path_job.mkdir(parents=True, exist_ok=True)

  # create jobs.json if not exists
  path_meta = Path(globals.odk_mailer_meta)

  if not path_meta.exists():
      path_meta.touch()

  if path_meta.stat().st_size == 0:
      path_meta.write_text("[]")

  if not is_json(path_meta.read_text()):
      raise typer.Exit(f"The file at '{path_meta}' is invalid.\n") 

def is_json(myjson):
  try:
    json.loads(myjson)
  except ValueError as e:
    return False
  return True