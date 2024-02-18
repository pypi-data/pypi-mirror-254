import typer
from typing import Optional
from typing_extensions import Annotated
from odk_mailer import commands, before
from odk_mailer.classes.Config import Config
import importlib.metadata
from dotenv import load_dotenv

load_dotenv()

app = typer.Typer(
    add_completion=False, 
    pretty_exceptions_enable=True,
    invoke_without_command=True,
    no_args_is_help=True
)
jobs_app= typer.Typer(
    invoke_without_command=True,
    no_args_is_help=True
)
app.add_typer(jobs_app, name="jobs", help="Manage mailjobs")

# settings_app= typer.Typer(
#     invoke_without_command=True,
#     no_args_is_help=True    
# )
# app.add_typer(settings_app, name="settings", help="Manage settings")

crontab_app = typer.Typer(
    invoke_without_command=True,
    no_args_is_help=True
)
app.add_typer(crontab_app, name="cron", help="Manage crontabs")


@app.callback()
def callback(
    version: Annotated[
        Optional[bool], typer.Option("--version", is_eager=True, help="Show version information and exit")
    ] = False,
    config: Annotated[
        Optional[bool], typer.Option("--config", help="Show config information and exit")
    ] = False,
    logs: Annotated[
        Optional[bool], typer.Option("--logs", help="Show live log")
    ] = False,
    ):
    """
    ODK Mailer

    Setup mail jobs by fetching recipients from CSV files or ODK API.

    Run mail jobs immediately or schedule them to be run over time.

    Evaluate available Mailjobs.

    """
    if version: 
        version = importlib.metadata.version('odk_mailer')
        print(version)
        typer.Exit()

    if config:
        config = Config()
        config.print()
        typer.Exit()

    if logs:
        commands.logs()
        raise typer.Exit()


    before.init()

@jobs_app.command("create")
def create(
    source: Annotated[Optional[str], typer.Option("--source", "-s", help="Define source as [type:path|url|api]::[location:str]")]= "",
    fields: Annotated[Optional[str], typer.Option("--fields", "-f", help="Define fields as [email:str]::[data: 'field_1,field_2']")]= "",
    message: Annotated[Optional[str], typer.Option("--message", "-m", help="Define message as [sender:str]::[subject:str]::[source:'stdin'|'path'|'url']::[location:str]::[type:'plain'|'html']")]= "",
    schedule: Annotated[Optional[str], typer.Option("--schedule", help="Define schedule as 'now' or [time:str] in 'YYYY-MM-DD HH:mm' format")]= "",
):
    """
    Create mail job
    """
    commands.create(source, fields, message, schedule)

@jobs_app.command("run")
def run(
    hash: Annotated[str, typer.Argument(help="Hash or id of mailjob to be run")],
    dry: Annotated[bool, typer.Option("--dry", help="Dry run - without sending mails.")] = False,
    verbose: Annotated[bool, typer.Option("--verbose", help="Print out smtp debugging information")] = False,
):
    """
    Run mail job
    """
    commands.run(hash, dry, verbose)

@jobs_app.command("delete")
def delete(
    id: Annotated[str, typer.Argument(help="Hexadecimal hash")]
):
    """
    Delete mail job
    """
    commands.delete(id)

@jobs_app.command()
def list():
    """
    List mail jobs
    """    
    commands.list_jobs()

@jobs_app.command()
def evaluate(
    force: Annotated[bool, typer.Option("--force", help="Enforce to run evaluated mailjobs")] = False,
    dry: Annotated[bool, typer.Option("--dry", help="Dry run without sending mails")] = False,
    verbose: Annotated[bool, typer.Option("--verbose", help="Print out additional SMTP information")] = False,
    notify: Annotated[bool, typer.Option("--notify", help="Notify over email about run state")] = False
):
    """
    Evaluate mail jobs
    """
    commands.evaluate(force, dry, verbose, notify)

@app.command()
def test(
    sender: Annotated[str, typer.Option("--sender")] = "ODK-Mailer <odk-mailer@freesmtpservers.com>",
    recipient: Annotated[str, typer.Option("--recipient")] = "foo@bcrontar.com",
    host: Annotated[str, typer.Option("--host")] = "smtp.freesmtpservers.com",
    port: Annotated[str, typer.Option("--port")] = "25",
    username: Annotated[str, typer.Option("--user")] = "",
    password: Annotated[str, typer.Option("--pass")] = ""
):
    """
    Send test mail
    """
    commands.test(sender, recipient, host, port, username, password)

@crontab_app.command("show")
def crontab_show():
    """
    Show crontab for odk-mailer
    """
    commands.crontab_show()

@crontab_app.command("init")
def crontab_init():
    """
    Initialize crontab
    """
    commands.crontab_init()

@crontab_app.command("clear")
def crontab_clear():
    """
    Clear all crontabs
    """
    commands.crontab_clear()

@crontab_app.command("enable")
def crontab_enable():
    """
    Enable crontab for odk-mailer
    """
    commands.crontab_enable()

@crontab_app.command("disable")
def crontab_disable():
    """
    Enable crontab for odk-mailer
    """
    commands.crontab_disable()