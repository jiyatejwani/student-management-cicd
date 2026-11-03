from dataclasses import dataclass, asdict
from threading import Lock


@dataclass
class Student:
    id: int
    name: str
    roll_number: str
    branch: str
    email: str

    def to_dict(self):
        return asdict(self)


class StudentRepository:
    """In-memory store. Can be swapped for a database later without touching routes."""

    def __init__(self):
        self._students = {}
        self._next_id = 1
        self._lock = Lock()

    def list_all(self):
        return [s.to_dict() for s in self._students.values()]

    def get(self, student_id):
        student = self._students.get(student_id)
        return student.to_dict() if student else None

    def add(self, data):
        self._validate(data)
        with self._lock:
            student = Student(
                id=self._next_id,
                name=data["name"],
                roll_number=data["roll_number"],
                branch=data["branch"],
                email=data["email"],
            )
            self._students[self._next_id] = student
            self._next_id += 1
        return student.to_dict()

    def update(self, student_id, data):
        if student_id not in self._students:
            return None
        self._validate(data)
        s = self._students[student_id]
        s.name, s.roll_number, s.branch, s.email = (
            data["name"], data["roll_number"], data["branch"], data["email"]
        )
        return s.to_dict()

    def delete(self, student_id):
        return self._students.pop(student_id, None) is not None

    @staticmethod
    def _validate(data):
        required = ["name", "roll_number", "branch", "email"]
        missing = [f for f in required if not data.get(f)]
        if missing:
            raise ValueError(f"Missing required fields: {', '.join(missing)}")
        if "@" not in data["email"]:
            raise ValueError("Invalid email address")


repository = StudentRepository()
