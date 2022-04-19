import datetime
from dataclasses import dataclass


@dataclass
class LogFile:
    file: str
    processed: str


@dataclass
class Log:
    ip: str
    indent: str
    user: str
    time: datetime.datetime
    method: str
    url: str
    protocol: str
    status: str
    size: str
    referrer: str
    agent: str
    other: str
