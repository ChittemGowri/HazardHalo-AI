import csv, io
from fastapi import APIRouter, Depends, Header, HTTPException, Response
from ..database import connection
from ..models import EventIn
from ..config import settings
router=APIRouter()
def authenticated(authorization:str|None=Header(default=None)):
    if not settings.api_token or authorization != f'Bearer {settings.api_token}': raise HTTPException(401,'invalid ingestion token')
@router.post('/api/v1/events',status_code=201,dependencies=[Depends(authenticated)])
def create_event(event:EventIn):
    with connection() as db:
        try: db.execute('INSERT INTO events VALUES(?,?,?,?,?,?,?,?,?)',(event.event_id,event.timestamp.isoformat(),event.event_type,event.severity,event.zone,event.message,event.source,event.mode,event.device_acknowledged)); db.commit()
        except Exception as e:
            if 'UNIQUE constraint' in str(e): return {'event_id':event.event_id,'duplicate':True}
            raise
    return {'event_id':event.event_id,'duplicate':False}
@router.get('/api/events')
def events(q:str='',limit:int=100):
    limit=max(1,min(limit,500)); with_conn=connection()
    with with_conn as db: rows=db.execute('SELECT * FROM events WHERE zone LIKE ? OR event_type LIKE ? OR message LIKE ? ORDER BY timestamp DESC LIMIT ?',tuple([f'%{q}%']*3+[limit])).fetchall()
    return [dict(row) for row in rows]
@router.get('/api/v1/export.json')
def export_json(): return events(limit=500)
@router.get('/api/v1/export.csv')
def export_csv():
    rows=events(limit=500); out=io.StringIO(); writer=csv.DictWriter(out,fieldnames=['event_id','timestamp','event_type','severity','zone','message','source','mode','device_acknowledged']); writer.writeheader(); writer.writerows(rows)
    return Response(out.getvalue(),media_type='text/csv',headers={'Content-Disposition':'attachment; filename=hazardhalo-events.csv'})
