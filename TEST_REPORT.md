# Test report

## 2026-10-15
- `python -m pip install fastapi uvicorn pydantic httpx pytest pyyaml pyserial`: **FAILED**. PyPI network access returned Windows socket error 10013.
- Automated tests: **NOT RUN** because pytest and FastAPI were not installable in this environment.
- `python -m compileall -q app edge_agent`: **PASSED**.
- Direct zone-engine alert/clear smoke test: **PASSED**.
- Hardware tests: **NOT RUN**; no verified PipeGen, FirmGen, CUDA, ESP-IDF, board, serial port, or camera access.

No simulated result is represented as a hardware result.
