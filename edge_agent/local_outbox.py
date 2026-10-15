import json
from pathlib import Path
class LocalOutbox:
    def __init__(self,path,max_items=500): self.path=Path(path); self.max_items=max_items; self.path.parent.mkdir(parents=True,exist_ok=True)
    def _read(self):
        try: return json.loads(self.path.read_text())
        except (OSError,json.JSONDecodeError): return []
    def add(self,event):
        items=self._read()+[event]; self.path.write_text(json.dumps(items[-self.max_items:])); return len(items)
    def pop_all(self):
        items=self._read(); self.path.write_text("[]"); return items
