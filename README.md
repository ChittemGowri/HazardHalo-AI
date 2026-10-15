# HazardHalo AI

Working software core for a privacy-conscious restricted-zone monitoring prototype. It has a FastAPI dashboard/API, local SQLite storage, a normalized polygon decision engine, serial protocol bridge, local cloud-upload outbox, and deployment container. It is not a certified safety system.

## Run locally

```powershell
python -m pip install -r requirements.txt
$env:HAZARDHALO_API_TOKEN='a-long-random-token'
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Open `http://localhost:8000`; API documentation is at `/docs`. Run `python -m pytest -q` before delivery. Set edge environment variables from `.env.example`; its cloud target must be HTTPS.

## Truthful integration status

The dashboard and edge core are implemented but were not launched here because dependencies could not be downloaded. The zone engine smoke test and all-module syntax compilation passed. PipeGen, FirmGen, TensorRT, ESP-IDF, ESP32 serial operation, camera inference, and a public deployment are not verified and are blocked as listed in `BLOCKERS.md`.

See `docs/DEPLOYMENT.md`, `docs/PIPEGEN_SETUP.md`, `docs/FIRMGEN_SETUP.md`, and `evidence/README.md` for reproducible next steps.
