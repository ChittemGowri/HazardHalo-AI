from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from uuid import uuid4

@dataclass
class Event:
    event_id:str; timestamp:str; event_type:str; severity:str; zone:str; message:str; source:str="edge_agent"; mode:str="real"; device_acknowledged:bool=False
    def payload(self): return asdict(self)

def new_event(event_type, zone, message, severity="HIGH", mode="real"):
    return Event(str(uuid4()),datetime.now(timezone.utc).isoformat(),event_type,severity,zone,message,mode=mode)
