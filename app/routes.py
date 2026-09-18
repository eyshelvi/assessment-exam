from flask import Blueprint, jsonify, render_template, request

from .data import REQUESTS, VALID_ASSIGNEES

bp = Blueprint("queue", __name__)
VALID_STATUSES = {"open", "in_progress", "resolved"}


def filter_requests(items, status=None, assignee=None):
    filtered = list(items)
    status_value = (status or "").strip().lower()
    assignee_value = (assignee or "").strip().lower()

    if status_value and status_value != "all" and status_value not in VALID_STATUSES:
        raise ValueError("status must be open, in_progress, or resolved")
    if status_value and status_value != "all":
        filtered = [item for item in filtered if item.get("status") == status_value]

    if assignee_value and assignee_value != "all":
        if assignee_value == "unassigned":
            filtered = [item for item in filtered if item.get("assignee") is None]
        elif assignee_value not in VALID_ASSIGNEES:
            raise ValueError("assignee must be one of: alice, bob, carol, all, or unassigned")
        else:
            filtered = [item for item in filtered if item.get("assignee") == assignee_value]

    return filtered


@bp.get("/")
def queue_page():
    status = request.args.get("status", "all")
    assignee = request.args.get("assignee", "all")
    try:
        requests = filter_requests(REQUESTS, status=status, assignee=assignee)
    except ValueError as exc:
        requests = REQUESTS
        status = "all"
        assignee = "all"
    return render_template(
        "queue.html",
        requests=requests,
        status=status,
        assignee=assignee,
        assignee_options=["alice", "bob", "carol"],
    )


@bp.get("/api/requests")
def list_requests():
    status = request.args.get("status", "all")
    assignee = request.args.get("assignee", "all")
    try:
        requests = filter_requests(REQUESTS, status=status, assignee=assignee)
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400
    return jsonify({"requests": requests})


@bp.patch("/api/requests/<int:request_id>/status")
def update_status(request_id):
    payload = request.get_json(silent=True) or {}
    status = payload.get("status")
    if status not in VALID_STATUSES:
        return jsonify({"error": "status must be open, in_progress, or resolved"}), 400

    for support_request in REQUESTS:
        if support_request["id"] == request_id:
            support_request["status"] = status
            return jsonify({"request": support_request})

    return jsonify({"error": "request not found"}), 404


@bp.patch("/api/requests/<int:request_id>/assignee")
def update_assignee(request_id):
    payload = request.get_json(silent=True) or {}
    if not isinstance(payload, dict):
        return jsonify({"error": "assignee must be a JSON object with assignee set to one of: alice, bob, carol, or null"}), 400
    if "assignee" not in payload:
        return jsonify({"error": "assignee is required and must be one of: alice, bob, carol, or null"}), 400

    assignee = payload.get("assignee")
    if assignee is None:
        assignee_value = None
    elif not isinstance(assignee, str):
        return jsonify({"error": "assignee must be one of: alice, bob, carol, or null"}), 400
    else:
        assignee_value = assignee.strip().lower()
        if not assignee_value:
            return jsonify({"error": "assignee must be one of: alice, bob, carol, or null"}), 400
        if assignee_value not in VALID_ASSIGNEES:
            return jsonify({"error": "assignee must be one of: alice, bob, carol, or null"}), 400

    for support_request in REQUESTS:
        if support_request["id"] == request_id:
            support_request["assignee"] = assignee_value
            return jsonify({"request": support_request})

    return jsonify({"error": "request not found"}), 404
