import sys
from models import Student, Classroom
from analytics import (
    top_student,
    lowest_student,
    rank_students,
    grade_distribution,
)
from utils import (
    load_students_from_csv,
    save_students_to_csv,
    validate_non_empty,
    validate_grade,
)



def operations():
    print("\n--- Operations ---")
    print("Add student chose 1")
    print("Remove student chose 2")
    print("Search student chose 3")
    print("Show average for classroom chose 4")
    print("Top/Lowest student chose 5")
    print("Rank students chose 6")
    print("Grade distribution chose 7")
    print("Save and exit chose 8")


def main():
    classroom = load_students_from_csv("data.csv")

    while True:
        operations()
        choice = input("Chose an option: ").strip()
        if choice == "1":
            name = validate_non_empty("Name: ")
            student_id = validate_non_empty("ID: ")
            grades = []
            while True:
                more = input("Add a grade? (y/n): ").strip().lower()
                if more == "y":
                    grade = validate_grade("Grade (0-100): ")
                    grades.append(grade)
                else:
                    break
            student = Student(name, student_id, grades)
            classroom.add_student(student)
            print("Student added.")
        elif choice == "2":
            sid = validate_non_empty("Student ID to remove: ")
            if classroom.remove_student(sid):
                print("Removed.")
            else:
                print("Student not found.")
        elif choice == "3":
            sid = input("Student ID to search: ")
            s = classroom.search_student(sid)
            if s:
                print(f"{s.name} ({s.student_id}) avg={s.average():.2f} cat={s.grade_category()}")
            else:
                print("Not found.")
        elif choice == "4":
            print(f"Class avg: {classroom.classroom_average():.2f}")
        elif choice == "5":
            top = top_student(classroom)
            low = lowest_student(classroom)
            if top:
                print(f"Top: {top.name} {top.average():.2f}")
            if low:
                print(f"Lowest: {low.name} {low.average():.2f}")
        elif choice == "6":
            ranked = rank_students(classroom)
            for idx, s in enumerate(ranked, start=1):
                print(f"{idx}. {s.name} - {s.average():.2f}")
        elif choice == "7":
            dist = grade_distribution(classroom)
            for cat, count in dist.items():
                print(f"{cat}: {count}")
        elif choice == "8":
            save_students_to_csv(classroom, "data.csv")
            print("Saved. Bye!")
            sys.exit(0)
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
