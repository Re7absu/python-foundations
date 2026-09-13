# comprehensions & dataclasses

from dataclasses import dataclass
from typing import Any

students: list[dict[str, Any]] = [
    {"name": "Ali", "grade": 85},
    {"name": "Sara", "grade": 92},
    {"name": "Rehab", "grade": 78},
    {"name": "Omar", "grade": 88},
]
passed_students = [student["name"] for student in students if student["grade"] >= 80]
print(passed_students)


@dataclass
class Student:
    name: str
    grade: float

    def display(self) -> str:
        return f"{self.name}: {self.grade}"


student = Student("Rehab", 95)

print(student.display())
