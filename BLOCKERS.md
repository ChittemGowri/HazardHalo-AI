# Blockers

| Item | Status | Exact unblock action |
|---|---|---|
| Python dependencies | BLOCKED | Allow PyPI/network access, then run `python -m pip install -r requirements.txt`. |
| PipeGen 0.5.1 | BLOCKED | Provide installed PipeGen 0.5.1 and supported NVIDIA environment; preserve its actual output schema/artifacts. |
| NVIDIA/TensorRT | BLOCKED | Run on supported NVIDIA system with CUDA/TensorRT and a camera/video source. |
| FirmGen 0.4.1 / ESP-IDF 5.5 | BLOCKED | Provide installed tools and a verified supported ESP32 board/wiring. |
| ESP32 / serial | BLOCKED | Connect board; expose COM port and safely wire LEDs/buzzer with appropriate driver. |
| Online deployment | BLOCKED | Provide hosting account/authorization and API token; deploy Docker image then verify public `/api/health`. |
