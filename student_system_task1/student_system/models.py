class Student:
    def __init__(self, name: str, student_id: str, grades: list):
        self._name = name
        self._student_id = student_id
        self._grades = grades or []

    @property
    def name(self):
        return self._name

    @property
    def student_id(self):
        return self._student_id

    @property
    def grades(self):
        return self._grades

    def average(self) -> float:
        if not self._grades:
            return 0.0
        return sum(self._grades) / len(self._grades)

    def grade_category(self) -> str:
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data.get("name"), data.get("student_id"), data.get("grades", []))

    def to_dict(self) -> dict:
        return {"name": self._name, "student_id": self._student_id, "grades": self._grades}


class Classroom:
    def __init__(self):
        self._students = []

    @property
    def students(self):
        return list(self._students)

    def add_student(self, student: Student):
        self._students.append(student)

    def remove_student(self, student_id: str) -> bool:
        for s in self._students:
            if s.student_id == student_id:
                self._students.remove(s)
                return True
        return False

    def search_student(self, student_id: str):
        for s in self._students:
            if s.student_id == student_id:
                return s
        return None

    def classroom_average(self) -> float:
        if not self._students:
            return 0.0
        return sum(s.average() for s in self._students) / len(self._students)

    @classmethod
    def from_list(cls, students_data: list):
        classroom = cls()
        from models import Student
        for data in students_data:
            classroom.add_student(Student.from_dict(data))
        return classroom
