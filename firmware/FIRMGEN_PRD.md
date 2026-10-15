# FirmGen PRD — HazardHalo Alarm Controller

Target: ESP32 using ESP-IDF 5.5, generated and traceable through FirmGen 0.4.1.

F-001 startup initializes every output to non-alarm state and logs state. F-002 receives newline-delimited UART. F-003 `ALERT|event_id` enables red LED and driven buzzer, disables green LED. F-004 `CLEAR` disables buzzer/red and enables green. F-005 `PING` replies `PONG`. F-006 invalid commands log but cause no GPIO change. F-007 buzzer pattern uses non-blocking timing. F-008 emits `STATE|NORMAL|ALERT|FAULT`. F-009 handles incremental input. F-010 explicitly safely configures GPIO.

Safety: determine board pins and wiring before generation; use LED resistors and a transistor/driver for high-current buzzer. This is a PRD for real FirmGen review, not generated firmware.
