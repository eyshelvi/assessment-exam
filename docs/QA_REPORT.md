# QA report

## Scope and environment
- App/version or commit: local repository state after implementing ownership and filtering for the support queue
- Environment/browser: Windows 11 + Python 3.11 + Flask test client / UI checks
- What I explored:
  - queue page rendering
  - combined status + assignee filtering
  - assignment/unassignment in UI
  - JSON API validation and error handling
  - automated regression tests

## Coverage summary
| Area | Technique | Result | Notes |
|---|---|---|---|
| queue rendering | manual + automated | pass | page loads and shows filters and assignee controls |
| assignment | manual + API | pass | assignee can be set and cleared |
| filtering | manual + API | pass | status and assignee filters work together |
| validation | API tests | pass | malformed/unknown values return `400` / `404` |
| regression safety | automated | pass | 7 tests passed |

## Defects and risks
| ID | Severity | Priority | Status | Summary |
|---|---|---|---|---|
| QA-001 | Medium | Medium | fixed | Assignee data could not be set or cleared through the browser or API |
| QA-002 | Medium | Medium | fixed | Queue had no combined status/assignee filtering in the UI |
| QA-003 | Low | Low | noted | In-memory data resets when the app restarts |

### QA-001 — assignee management was missing
- **Steps to reproduce:** open the queue page and try to assign a request, or call `PATCH /api/requests/<id>/assignee` with a valid assignee JSON payload.
- **Expected result:** the request should receive an assignee or become unassigned cleanly.
- **Actual result:** the app had no assignee field or assignment endpoint, so no assignment could be stored.
- **Impact / rationale:** staff could not tell who owned a request or triage the queue by owner.
- **Evidence:** request records in `app/data.py` had no `assignee` field and the API had no `assignee` route.
- **Disposition:** fixed

### QA-002 — filters did not support queue narrowing by assignee or status together
- **Steps to reproduce:** attempt to filter the queue by status and assignee at the same time using the UI or `/api/requests` query parameters.
- **Expected result:** both filters apply together and an option exists to reset to the unfiltered queue.
- **Actual result:** there were no relevant filters or browser controls, and the API simply returned all requests.
- **Impact / rationale:** staff could not narrow the queue to actionable or owned work quickly.
- **Evidence:** the queue template had only a status dropdown per row and no filter form.
- **Disposition:** fixed

### QA-003 — data does not persist after restart
- **Steps to reproduce:** assign a request, restart the Flask process, and reload the queue.
- **Expected result:** request data remains stable across a restart.
- **Actual result:** the application resets in-memory seed data on restart.
- **Impact / rationale:** this is acceptable for the task because persistence was explicitly out of scope, but it is a product risk for real operational use.
- **Evidence:** the project intentionally uses in-memory data in `app/data.py` and the README notes this design.
- **Disposition:** noted / product decision outside scope

## Remaining risks / recommended follow-up
- Add database-backed persistence if the queue is expected to hold real operational data.
- Consider adding additional assignee names from a config file or admin-managed list.
- Capture a formal browser recording for stakeholder review before sign-off.
