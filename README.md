# Developer / QA Hybrid Assessment — Support Queue

This is the starter repository for a technical assessment. It is a deliberately small Flask application used by an internal support team to view and update support requests.

## Start here

Read [`docs/CANDIDATE_TASK.md`](docs/CANDIDATE_TASK.md) before changing code.

## Local setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
pytest -q
python run.py
```

Open `http://127.0.0.1:5056` in a browser. Use a different port only if 5056 is already in use.

## API contract

The queue exposes a small JSON API to assign or unassign support requests.

- `PATCH /api/requests/<id>/assignee`
  - Request body example: `{"assignee": "alice"}`
  - Unassign example: `{"assignee": null}`
  - Valid values: `alice`, `bob`, `carol`, or `null`
  - Success: `200` with the updated request object
  - Invalid payload: `400` with an error message
  - Missing request ID: `404`

## What to submit

Follow [`docs/SUBMISSION_CHECKLIST.md`](docs/SUBMISSION_CHECKLIST.md). Do not include virtual environments, secrets, or generated files.

## Notes

- The application uses in-memory seed data. Data resets when the process restarts.
- AI tooling is permitted; material use must be disclosed using the provided template.
