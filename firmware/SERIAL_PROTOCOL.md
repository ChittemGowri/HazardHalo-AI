# Serial protocol v1

ASCII, 115200 baud by default, newline (`\n`) terminated; bounded timeout required.

Commands: `ALERT|<event_id>`, `CLEAR`, `PING`, `HEARTBEAT`.

Responses: `ACK|ALERT|<event_id>`, `ACK|CLEAR`, `PONG`, `STATE|NORMAL`, `STATE|ALERT`, `STATE|FAULT`.

UART ACK records receipt only; it does not prove LED/buzzer physical behavior.
