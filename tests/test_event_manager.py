from edge_agent.event_manager import new_event
from edge_agent.local_outbox import LocalOutbox
def test_unique_event_ids_and_outbox(tmp_path):
 a,b=new_event('PERSON_IN_ZONE','z','m'),new_event('PERSON_IN_ZONE','z','m'); assert a.event_id != b.event_id
 o=LocalOutbox(tmp_path/'outbox.json'); o.add(a.payload()); assert o.pop_all()[0]['event_id']==a.event_id; assert o.pop_all()==[]
