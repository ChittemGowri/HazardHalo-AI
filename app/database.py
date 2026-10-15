import sqlite3
from pathlib import Path
from .config import settings
def connection():
    if not settings.database_url.startswith("sqlite:///"): raise RuntimeError("included database driver supports SQLite URLs only")
    path=Path(settings.database_url.removeprefix("sqlite:///")); path.parent.mkdir(parents=True,exist_ok=True)
    db=sqlite3.connect(path); db.row_factory=sqlite3.Row; return db
def initialize():
    with connection() as db:
        db.executescript('''CREATE TABLE IF NOT EXISTS events(event_id TEXT PRIMARY KEY,timestamp TEXT NOT NULL,event_type TEXT NOT NULL,severity TEXT NOT NULL,zone TEXT NOT NULL,message TEXT NOT NULL,source TEXT NOT NULL,mode TEXT NOT NULL,device_acknowledged INTEGER NOT NULL DEFAULT 0);
        CREATE TABLE IF NOT EXISTS heartbeats(component TEXT PRIMARY KEY,last_seen TEXT NOT NULL,state TEXT NOT NULL,details TEXT NOT NULL);''')
