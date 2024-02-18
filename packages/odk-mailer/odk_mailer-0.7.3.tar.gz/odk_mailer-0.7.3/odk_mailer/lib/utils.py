from rich import print
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.padding import Padding
from datetime import datetime
import typer
import time
import base64
import socket

# return unformatted string instead of raising error
# when key is missing within dictionary
# https://stackoverflow.com/a/17215533/3127170
class SafeDict(dict):
    def __missing__(self, key):
        return '{' + key + '}' 

def abort(msg):
    print("[bold red]Error:[/bold red] "+msg)
    raise typer.Abort()

def now():
    return int(time.time())

def ts_to_str(ts):
    dt = datetime.fromtimestamp(ts)
    return dt.strftime("%c")

def base64_encode_str(input_str: str):
    input_bytes = input_str.encode("ascii") 
    base64_bytes = base64.b64encode(input_bytes)

    return base64_bytes.decode("ascii")

def base64_decode_str(base64_str: str):
    base64_bytes = base64_str.encode("ascii") 
    output_bytes = base64.b64decode(base64_bytes)
    
    return output_bytes.decode("ascii")

def safe_format_map(text, dict):
    return text.format_map(SafeDict(vars(dict)))

def render_state(state):
    match state:
        case 0:
            return "pending"
        case 1: 
            return "success"
        case _:
            return "failure"

def print_jobs(jobsMeta):
    console = Console()
    header = ["Job Id", "Created","Scheduled", "Recipients", "State", "Note"]
    table = Table(*header, expand=False, highlight=True, box=None, title_justify="left", show_lines="True")
    console.print()
    for job in jobsMeta:
        row = []
        for key,val in job.items():
            if key == 'hash':
                row.append(val[:10])
            if key in ['created','scheduled']:
                row.append((ts_to_str(val)))
            if key== 'recipients':
                row.append(str(val))
            if key == 'state':
                row.append(render_state(val))
            if key == 'note':
                row.append(val)
        # data = [job["hash"], job["created"], job["scheduled"], job["state"], job["source"], job["title"]]
        # row.extend(data)
        table.add_row(*row)
    console.print(table)
    console.print()

def print_panel(data):
    print(Panel(data))

def print_mail(content):
    print(Padding(content, 1))

def print_success(msg):
        print(f"[bold green]✅ {msg}[/bold green]")


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP