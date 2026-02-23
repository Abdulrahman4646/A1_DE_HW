from models import Student, Classroom


def top_student(classroom: Classroom):
    if not classroom.students:
        return None
    return max(classroom.students, key=lambda s: s.average())


def lowest_student(classroom: Classroom):
    if not classroom.students:
        return None
    return min(classroom.students, key=lambda s: s.average())


def rank_students(classroom: Classroom, reverse: bool = True):
    return sorted(classroom.students, key=lambda s: s.average(), reverse=reverse)


def grade_distribution(classroom: Classroom) -> dict:
    dist = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for s in classroom.students:
        cat = s.grade_category()
        if cat in dist:
            dist[cat] += 1
    return dist
