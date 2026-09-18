from app.data import REQUESTS


def test_queue_page_loads(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Support request queue" in response.data


def test_queue_page_supports_combined_filters(client):
    REQUESTS[0]["assignee"] = "alice"
    REQUESTS[1]["assignee"] = "alice"
    REQUESTS[2]["assignee"] = "bob"

    response = client.get("/?status=open&assignee=alice")
    assert response.status_code == 200
    assert b"Cannot download monthly statement" in response.data
    assert b"Clear filters" in response.data
    assert b"All assignees" in response.data


def test_api_lists_seeded_requests(client):
    response = client.get("/api/requests")
    assert response.status_code == 200
    payload = response.get_json()
    assert len(payload["requests"]) == 3
    assert payload["requests"][0]["priority"] == "high"


def test_api_filters_requests_by_status_and_assignee(client):
    REQUESTS[0]["assignee"] = "alice"
    REQUESTS[1]["assignee"] = "alice"
    REQUESTS[2]["assignee"] = "bob"

    response = client.get("/api/requests?status=open&assignee=alice")
    assert response.status_code == 200
    payload = response.get_json()
    assert [request["id"] for request in payload["requests"]] == [1]


def test_api_updates_assignee_and_unassigns(client):
    response = client.patch("/api/requests/1/assignee", json={"assignee": "alice"})
    assert response.status_code == 200
    payload = response.get_json()
    assert payload["request"]["assignee"] == "alice"

    response = client.patch("/api/requests/1/assignee", json={"assignee": None})
    assert response.status_code == 200
    payload = response.get_json()
    assert payload["request"]["assignee"] is None


def test_api_rejects_invalid_assignee_payloads(client):
    response = client.patch("/api/requests/1/assignee", json={"assignee": "unknown"})
    assert response.status_code == 400
    assert "assignee" in response.get_json()["error"].lower()

    response = client.patch("/api/requests/1/assignee", json={"assignee": 5})
    assert response.status_code == 400


def test_api_reports_missing_request_for_assignment(client):
    response = client.patch("/api/requests/999/assignee", json={"assignee": "alice"})
    assert response.status_code == 404
    assert "request not found" in response.get_json()["error"].lower()
