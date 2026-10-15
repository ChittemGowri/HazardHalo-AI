# Decisions

- FastAPI serves API and static dashboard in one deployable process.
- SQLite is the local default; `HAZARDHALO_DATABASE_URL` permits a deployment-specific replacement, but the included driver intentionally supports SQLite only.
- Zone coordinates and bounding boxes are normalized (0..1); lower-center of a person box is evaluated.
- PipeGen metadata remains adapter-driven until a real verified PipeGen schema is available.
- UART protocol is newline-delimited ASCII and is shared by the bridge and firmware specification.
