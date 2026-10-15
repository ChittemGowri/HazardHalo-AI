# Architecture

`PipeGen metadata → adapter → zone engine → event manager → UART ESP32`, with the event manager also posting metadata to `FastAPI → SQLite → dashboard`. Cloud loss must not interrupt the UART path; failed cloud deliveries belong in the local outbox.
