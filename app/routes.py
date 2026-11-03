from flask import Blueprint, jsonify, request
from app.models import repository

students_bp = Blueprint("students", __name__)


@students_bp.get("/health")
def health():
    """Liveness check — used by the pipeline and the cloud host."""
    return jsonify({"status": "ok"}), 200


@students_bp.get("/students")
def list_students():
    return jsonify(repository.list_all()), 200


@students_bp.post("/students")
def create_student():
    data = request.get_json(silent=True) or {}
    try:
        return jsonify(repository.add(data)), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@students_bp.get("/students/<int:student_id>")
def get_student(student_id):
    student = repository.get(student_id)
    if student is None:
        return jsonify({"error": "Student not found"}), 404
    return jsonify(student), 200


@students_bp.put("/students/<int:student_id>")
def update_student(student_id):
    data = request.get_json(silent=True) or {}
    try:
        student = repository.update(student_id, data)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    if student is None:
        return jsonify({"error": "Student not found"}), 404
    return jsonify(student), 200


@students_bp.delete("/students/<int:student_id>")
def delete_student(student_id):
    if not repository.delete(student_id):
        return jsonify({"error": "Student not found"}), 404
    return jsonify({"message": "Student deleted"}), 200
