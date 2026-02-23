import csv
import json
from models import Student, Classroom


def load_students_from_csv(path: str) -> Classroom:
    classroom = Classroom()
    try:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                grades = [float(g) for g in row.get("grades", "").split(",") if g.strip()]
                student = Student(row["name"], row["student_id"], grades)
                classroom.add_student(student)
    except FileNotFoundError:
        pass
    return classroom


def save_students_to_csv(classroom: Classroom, path: str):
    with open(path, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["name", "student_id", "grades"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for s in classroom.students:
            grades_str = ",".join(str(g) for g in s.grades)
            writer.writerow({"name": s.name, "student_id": s.student_id, "grades": grades_str})


def validate_non_empty(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")


def validate_grade(prompt: str) -> float:
    while True:
        try:
            val = float(input(prompt))
            if 0 <= val <= 100:
                return val
            print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid number.")
