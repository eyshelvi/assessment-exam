# Support Request Queue

A small Flask application for an internal support team. The queue displays customer requests and lets support staff filter work, change its status, and assign or unassign ownership.

## Features

- View seeded support requests with customer, priority, assignee, and status information.
- Filter requests by status and assignee, including combined filters.
- Clear filters to return to the complete queue.
- Update status or assignee directly from the queue page.
- Use JSON endpoints for listing requests and updating request status or ownership.

## Requirements

- Python 3.9 or newer
- Flask 3.x
- pytest 8.x for tests

## Run locally

Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

macOS/Linux:

```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Start the application:

```bash
python run.py
```

Open <http://127.0.0.1:5056> in a browser. The development server uses port `5056`; edit `run.py` if another available port is required.

## API

All API responses are JSON. The fixed assignee list is `alice`, `bob`, and `carol`. A request may also be unassigned using `null`.

### List requests

```http
GET /api/requests
GET /api/requests?status=open&assignee=alice
```

Supported query values:

- `status`: `all`, `open`, `in_progress`, or `resolved`
- `assignee`: `all`, `unassigned`, `alice`, `bob`, or `carol`

Successful responses return `200` with an object containing a `requests` array. Invalid filter values return `400` with an `error` message.

### Update assignee

```http
PATCH /api/requests/1/assignee
Content-Type: application/json

{"assignee": "alice"}
```

Use `{"assignee": null}` to unassign a request. A successful update returns `200` with the updated request under `request`. Missing or invalid `assignee` values return `400`; an unknown request ID returns `404`.

### Update status

```http
PATCH /api/requests/1/status
Content-Type: application/json

{"status": "resolved"}
```

Valid statuses are `open`, `in_progress`, and `resolved`. Successful updates return `200`; invalid statuses return `400`; an unknown request ID returns `404`.

## Tests

Run the automated test suite with:

```bash
python -m pytest -q
```

The tests cover page rendering, combined filters, API filtering, assignment and unassignment, invalid payloads, and missing request IDs.

## Project layout

```text
app/
  data.py                 In-memory seed requests and assignee list
  routes.py               HTML routes and JSON API endpoints
  templates/queue.html    Queue UI and browser-side update requests
tests/                    Flask and API regression tests
docs/                     Implementation, QA, and submission notes
run.py                    Local development entry point
requirements.txt          Python dependencies
```

## Data and limitations

The application deliberately uses in-memory seed data. Changes made through the UI or API are lost when the process restarts, and there is no authentication or persistent database. These decisions keep the example small; production use would require persistence, access control, and an operational assignee-management strategy.

Additional implementation and QA context is available in [`docs/IMPLEMENTATION_NOTES.md`](docs/IMPLEMENTATION_NOTES.md) and [`docs/QA_REPORT.md`](docs/QA_REPORT.md).
