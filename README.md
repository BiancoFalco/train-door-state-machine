# Train Door State Machine

A small Python model of metro train door logic, tested with pytest and checked by GitHub Actions on every push.

## Rules
- Doors are released only at standstill (< 0.5 km/h) and at a platform.
- If an obstacle is detected while closing, the door reopens.
- Traction is allowed only when all doors are closed and locked (fail-safe interlock).

## Run locally
```
pip install pytest
pytest -v
```
