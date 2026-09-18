# AI-use disclosure

- **Tools used:** Copilot
- **Where AI materially influenced the work** (code, tests, investigation, documentation, etc.):
  - analyzed the starter app and the candidate requirements
  - proposed the assignee/filter data model and validation approach
  - generated the queue UI and API changes
  - drafted the automated tests and QA documentation
- **Representative prompts or interaction summary:**
  - Review the starter app and implement ownership and filtering per the candidate task.
  - Add validation for assignee payloads and ensure combined filter behavior works.
- **How I reviewed and validated output:**
  - Checked the API responses and filter behavior through the Flask test client and the running app.
- **What I changed or rejected after review:**
  - I rejected a more complex persistence design because the task explicitly says not to add persistence or external services.

