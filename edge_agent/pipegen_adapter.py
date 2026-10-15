"""Adapter for a verified PipeGen output schema, intentionally not speculative."""
import json
from datetime import datetime, timezone
from .zone_engine import Detection

class PipeGenAdapter:
    def __init__(self, schema="unverified_fixture"): self.schema=schema
    def parse(self, raw):
        if self.schema != "unverified_fixture": raise ValueError("No verified PipeGen schema configured")
        try: data=json.loads(raw) if isinstance(raw,str) else raw; items=data["detections"]
        except (TypeError, ValueError, KeyError) as e: raise ValueError("malformed fixture metadata") from e
        result=[]
        for item in items:
            try:
                box=tuple(float(item[k]) for k in ("x","y","width","height")); confidence=float(item["confidence"])
                result.append(Detection(str(item["label"]),confidence,box,datetime.fromisoformat(item.get("timestamp",datetime.now(timezone.utc).isoformat())),str(item.get("source","fixture")),item.get("track_id")))
            except (KeyError,TypeError,ValueError): continue
        return result
