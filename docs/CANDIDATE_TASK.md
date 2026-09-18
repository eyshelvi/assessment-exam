# Candidate task — Add ownership and usable queue filtering

You have joined a team maintaining a small internal support-request queue. The product owner has reported that requests are difficult to triage because no one can see ownership or narrow the queue.

## Required outcome

Implement the following while preserving existing behavior:

1. **Assignment:** Each support request must have an optional assignee. Support staff must be able to assign or unassign a request from the UI.
2. **Filtering:** Add UI controls to filter the displayed queue by **status** and **assignee**. Filters must work together and include a clear way to return to the unfiltered queue.
3. **API:** Expose the assignment capability through a documented JSON API endpoint. Validate malformed input and return meaningful HTTP status codes/errors.
4. **Quality:** Add focused automated tests for the new behavior and relevant validation/error paths.
5. **Documentation:** Provide the requested QA report, implementation notes, and AI-use disclosure.
6. **Walkthrough recording:** Create a concise **5–10 minute** screen recording that demonstrates the completed feature, briefly explains your implementation and test/QA approach, and calls out any known limitations or risks. Share it as a viewable link with your submission.

You may choose a simple fixed list of assignees, provided the decision is documented. Do not add authentication, persistence, external services, or deployment unless you have a specific reason and have time.

## QA expectation

Treat the starter app as an unfamiliar system. Conduct exploratory/manual QA in addition to automated tests. Log defects or risks you identify—even if you do not fix them—and prioritize them using the supplied template. You may fix defects beyond the requested feature if you explain the rationale and protect the change with tests.

## Evaluation focus

We assess correctness, maintainability, test selection, risk-based QA, documentation quality, and transparent use of AI. We do **not** assess visual polish, framework novelty, or the number of tests alone.

## Boundaries

- AI tools are allowed. Validate their output yourself.
- Do not use real customer data, credentials, or hosted services.
- Keep dependencies justified and minimal.
- Record assumptions rather than silently making product decisions.
