import logging
from pathlib import Path
import typer
import time
import os

# tbd: redirect smtp debug to log file: https://stackoverflow.com/a/7303587/3127170

FILE_NAME_LOG = 'odk-mailer.log'
APP_NAME = 'odk-mailer'
app_dir=typer.get_app_dir(APP_NAME, force_posix=True)
log_path: Path = Path(app_dir) / FILE_NAME_LOG

logging.basicConfig(
    filename=log_path, 
    encoding='utf-8', 
    level=logging.DEBUG, 
    format='%(asctime)s: %(levelname)s: %(message)s'
)

def write(msg, type="info"):

    if type == "info":
        logging.info(msg)

    if type=="error":
        logging.error(msg)


def read():
    def follow(thefile):
        '''generator function that yields new lines in a file
        '''
        # seek the end of the file
        thefile.seek(0, os.SEEK_END)
        
        # start infinite loop
        while True:
            # read last line of file
            line = thefile.readline()
            if not line:
                time.sleep(0.1)
                continue
            yield line
    
    logfile = open(log_path,"r")
    loglines = follow(logfile)
    
    print(f"Following on logfile: {log_path}..")
    print("[Press ctrl + c to exit]")
    for line in loglines:
        print(line)