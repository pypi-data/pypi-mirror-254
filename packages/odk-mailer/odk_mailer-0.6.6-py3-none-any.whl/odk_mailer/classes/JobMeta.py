class JobMeta:
    hash: str
    created: int
    scheduled: int
    recipients: int
    state: int
    note: str

    def __init__(self, mailjob) -> None:
        
        self.hash = mailjob.hash
        self.created = mailjob.created
        self.scheduled = mailjob.schedule.timestamp
        self.recipients = len(mailjob.recipients)
        self.state = 0
        if mailjob.message.source == 'stdin':
            self.note = "stdin"
        else: 
            self.note = mailjob.message.location
