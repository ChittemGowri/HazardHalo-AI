from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .database import initialize
from .api.health import router as health_router
from .api.events import router as events_router
from .api.status import router as status_router
app=FastAPI(title='HazardHalo AI',version='0.1.0')
@app.on_event('startup')
def startup(): initialize()
app.include_router(health_router); app.include_router(events_router); app.include_router(status_router)
app.mount('/',StaticFiles(directory=Path(__file__).parent/'static',html=True),name='dashboard')
