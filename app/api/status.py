from datetime import datetime, timezone
from fastapi import APIRouter, Depends, Header, HTTPException
from ..database import connection
from ..models import HeartbeatIn
from .events import authenticated
router=APIRouter()
@router.post('/api/v1/heartbeat',dependencies=[Depends(authenticated)])
def heartbeat(body:HeartbeatIn):
    now=datetime.now(timezone.utc).isoformat()
    with connection() as db: db.execute('INSERT OR REPLACE INTO heartbeats VALUES(?,?,?,?)',(body.component,now,body.state,body.details)); db.commit()
    return {'accepted':True,'timestamp':now}
@router.get('/api/status')
def status():
    with connection() as db:
        records={r['component']:dict(r) for r in db.execute('SELECT * FROM heartbeats')}; total=db.execute('SELECT count(*) FROM events').fetchone()[0]; today=db.execute("SELECT count(*) FROM events WHERE timestamp >= date('now')").fetchone()[0]; latest=db.execute('SELECT * FROM events ORDER BY timestamp DESC LIMIT 1').fetchone()
    return {'backend':'CONNECTED','components':{k:records.get(k,{'state':'UNKNOWN','last_seen':None}) for k in ('edge_agent','pipegen','esp32')},'total_incidents':total,'today_incidents':today,'latest_event':dict(latest) if latest else None}
