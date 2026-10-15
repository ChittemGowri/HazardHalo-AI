# Deployment

1. In a network-enabled environment run `python -m pip install -r requirements.txt`.
2. Set `HAZARDHALO_API_TOKEN` and a persistent `HAZARDHALO_DATABASE_URL` path; do not use the sample value.
3. Local run: `uvicorn app.main:app --host 0.0.0.0 --port 8000`.
4. Container: `docker build -t hazardhalo .`; deploy it to an authorized service with `PORT`, token, and persistent storage.
5. Verify the public `https://host/api/health` before claiming deployment. Most free containers have ephemeral disks; use an approved persistent database/volume for retention.

The hosted service never accesses the local camera, GPU, or USB ESP32.
