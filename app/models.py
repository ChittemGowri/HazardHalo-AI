from datetime import datetime
from typing import Literal
from pydantic import BaseModel, Field
class EventIn(BaseModel):
    event_id:str=Field(min_length=8,max_length=128); timestamp:datetime; event_type:Literal['PERSON_IN_ZONE','ZONE_CLEARED','VISION_INPUT_STALE','SERIAL_DISCONNECTED','EDGE_AGENT_STATUS']; severity:Literal['LOW','MEDIUM','HIGH','CRITICAL']; zone:str=Field(min_length=1,max_length=100); message:str=Field(min_length=1,max_length=500); source:str=Field(default='edge_agent',max_length=100); mode:Literal['real','simulated']='real'; device_acknowledged:bool=False
class HeartbeatIn(BaseModel):
    component:Literal['edge_agent','pipegen','esp32']; state:Literal['CONNECTED','STALE','DISCONNECTED','SIMULATED','UNKNOWN']; details:str=Field(default='',max_length=500)
