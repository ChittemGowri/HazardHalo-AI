"""Metadata-only HTTPS client; failures are reported to caller for outbox queueing."""
import json
from urllib.request import Request, urlopen
class CloudClient:
    def __init__(self, base_url, token, timeout=5): self.base_url=base_url.rstrip('/'); self.token=token; self.timeout=timeout
    def post_event(self,event): return self._post('/api/v1/events',event)
    def heartbeat(self,body): return self._post('/api/v1/heartbeat',body)
    def _post(self,path,body):
        if not self.base_url.startswith('https://'): raise ValueError('cloud API must use HTTPS')
        data=json.dumps(body).encode(); req=Request(self.base_url+path,data=data,headers={'Authorization':'Bearer '+self.token,'Content-Type':'application/json'},method='POST')
        with urlopen(req,timeout=self.timeout) as response: return json.loads(response.read())
