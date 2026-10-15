"""Minimal edge loop entrypoint; wire a verified PipeGen reader before real use."""
import os
from .local_outbox import LocalOutbox
from .cloud_client import CloudClient
def flush_outbox():
    outbox=LocalOutbox(os.getenv('HAZARDHALO_OUTBOX','edge_agent/outbox.json')); client=CloudClient(os.environ['HAZARDHALO_API_BASE_URL'],os.environ['HAZARDHALO_EDGE_TOKEN'])
    pending=outbox.pop_all()
    for event in pending:
        try: client.post_event(event)
        except Exception: outbox.add(event)
if __name__=='__main__': flush_outbox()
