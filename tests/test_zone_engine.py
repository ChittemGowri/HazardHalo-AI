from datetime import datetime, timedelta, timezone
from edge_agent.zone_engine import *
def d(x,y,c=.9): return Detection('person',c,(x,y,.1,.1),datetime.now(timezone.utc))
def engine(): return ZoneEngine(ZoneConfig('z',((.2,.2),(.8,.2),(.8,.8),(.2,.8)),.5,1,1,0))
def test_alert_and_clear():
 e=engine(); t=datetime.now(timezone.utc); assert not e.evaluate([d(.3,.3)],t); assert e.evaluate([d(.3,.3)],t+timedelta(seconds=1))==['PERSON_IN_ZONE']; assert not e.evaluate([],t+timedelta(seconds=1)); assert e.evaluate([],t+timedelta(seconds=2))==['ZONE_CLEARED']
def test_outside_low_and_boundary():
 e=engine(); t=datetime.now(timezone.utc); assert not e.evaluate([d(.01,.01),d(.3,.3,.1)],t+timedelta(seconds=2)); assert point_in_polygon((.2,.5),e.config.polygon)
