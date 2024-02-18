# ODK Mailer

A simple CLI to send Mails for ODK.
Built with Typer and packaged with Poetry.

## Requirements
- Python 3
- PIP
- cron

## Setup
**Install the cli via pip**
```bash
pip install odk-mailer
```

**Configuration example**
Config location: `~/.env`:
```
    SMTP_HOST=smtp.freesmtpservers.com
    SMTP_PORT=25
    SMTP_USER=
    SMTP_PASS=
    CRON_FREQUENCY=15
    NOTIFY_TO=foo@bar.com,faz@baz.com
    NOTIFY_FROM=odk-mailer@freesmtpservers.com
    ODK_HOST=https://your.odk-central.host.tld
```

## Usage
**Create and run a new mail job**
```bash
    # Create a new mail job with a unique ID
    odk-mailer jobs create

    # Run the job by ID
    odk-mailer jobs run <job-id>

    # Remove a job
    odk-mailer jobs delete <job-id>
```

**List mail jobs and evaluate them**
```bash
    # Show all jobs
    odk-mailer jobs list

    # Run all jobs that are ready to be sent
    odk-mailer jobs evaluate
```

**Initiate crontab to periodically evaluate mailjobs and run them directly after**
```bash
    odk-mailer cron init
```

## Development
Building a Package - Guide: https://typer.tiangolo.com/tutorial/package/#create-your-app

**Requirements**
- Python 3.10
- Poetry 1.7

```bash
    # clone the repo and cd into
    poetry shell
    poetry install
    # Run it with
    poetry run odk-mailer 
```

**Push to PyPi**

```
    poetry build
    poetry publish
    # requires credentials to be setup: poetry config pypi-token.pypi <my-token>
```