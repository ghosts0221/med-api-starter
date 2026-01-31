# med-api-starter (FastAPI)

Minimal FastAPI REST API demonstrating:
- JSON request/response
- SQLite CRUD with SQLAlchemy
- Tests (pytest)
- CI via GitHub Actions

> Dummy data only. No real patient information.

## Quickstart (No Docker)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:
- http://127.0.0.1:8000/docs

## Tests
```bash
pytest -q
```
