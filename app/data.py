VALID_ASSIGNEES = ["alice", "bob", "carol"]

REQUESTS = [
    {"id": 1, "title": "Cannot download monthly statement", "customer_email": "ava@example.test", "priority": "high", "status": "open", "assignee": "alice"},
    {"id": 2, "title": "Update billing address", "customer_email": "noah@example.test", "priority": "low", "status": "in_progress", "assignee": None},
    {"id": 3, "title": "Card payment appears twice", "customer_email": "mia@example.test", "priority": "high", "status": "open", "assignee": "bob"},
]


def reset_requests():
    global REQUESTS
    REQUESTS = [
        {"id": 1, "title": "Cannot download monthly statement", "customer_email": "ava@example.test", "priority": "high", "status": "open", "assignee": "alice"},
        {"id": 2, "title": "Update billing address", "customer_email": "noah@example.test", "priority": "low", "status": "in_progress", "assignee": None},
        {"id": 3, "title": "Card payment appears twice", "customer_email": "mia@example.test", "priority": "high", "status": "open", "assignee": "bob"},
    ]
