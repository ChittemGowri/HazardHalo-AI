# HazardHalo AI

HazardHalo is a non-certified workplace restricted-zone monitoring prototype. A local edge agent consumes person-detection metadata, evaluates a normalized polygon zone, operates an ESP32 alarm over serial, and uploads metadata-only events to a FastAPI dashboard. No video or biometric identity is retained or uploaded.

Acceptance core: authenticated, idempotent event API; SQLite event history; dashboard; deterministic occupancy engine; serial protocol bridge; durable local outbox; automated unit tests; container deployment configuration.
