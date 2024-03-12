from models import Library, Employee, Order, Book


def main():
    library1 = Library("Warsaw",
                       "Library St.",
                       "00-000",
                       "9:00-17:00",
                       "123456789")
    library2 = Library("Cracow",
                       "Library St.",
                       "11-111",
                       "9:30-18:00",
                       "234567890")

    publication_date1 = "2020-01-01"
    book1 = Book(library1, publication_date1, "John", "Doe", 150)
    book2 = Book(library1, publication_date1, "Jane", "Austen", 250)
    book3 = Book(library2, publication_date1, "George", "Orwell", 300)
    book4 = Book(library2, publication_date1, "Leo", "Tolstoy", 400)
    book5 = Book(library2, publication_date1, "Virginia", "Woolf", 350)

    hire_date1 = "2018-01-01"
    employee1 = Employee("Alice",
                         "Smith", hire_date1,
                         "1990-01-01",
                         "Warsaw",
                         "Employee St.",
                         "00-000",
                         "111111111")
    employee2 = Employee("Bob",
                         "Johnson",
                         hire_date1,
                         "1985-01-01",
                         "Warsaw",
                         "Employee St.",
                         "00-000",
                         "222222222")

    student1 = "Student1"
    student2 = "Student2"

    order1_books = [book1, book2, book3]
    order1_date = "2022-01-01"
    order1 = Order(employee1, student1, order1_books, order1_date)

    order2_books = [book4, book5]
    order2_date = "2022-01-02"
    order2 = Order(employee2, student2, order2_books, order2_date)

    print(order1)
    print()
    print(order2)


if __name__ == "__main__":
    main()
