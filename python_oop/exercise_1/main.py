from models import Student


def main():
    student1 = Student("Alice", [60, 70, 80])
    student2 = Student("Bob", [40, 45, 50])

    print(f"Student '{student1.name}' "
          f"{'' if student1.is_passed() else 'did not'} pass the exam.")
    print(f"Student '{student2.name}' "
          f"{'' if student2.is_passed() else 'did not'} pass the exam.")


if __name__ == "__main__":
    main()
