class Library:
    def __init__(self, city: str,
                 street: str, zip_code: str,
                 open_hours: str, phone: str):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (f"Library at {self.street}, "
                f"{self.zip_code}, "
                f"{self.city}\nOpen Hours: "
                f"{self.open_hours}\nPhone: {self.phone}")


class Employee:
    def __init__(self, first_name: str, last_name: str,
                 hire_date: str, birth_date: str,
                 city: str, street: str,
                 zip_code: str, phone: str):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (f"Employee "
                f"{self.first_name} "
                f"{self.last_name}\nHire Date: "
                f"{self.hire_date}\nBirth Date: "
                f"{self.birth_date}\nAddress: {self.street}, "
                f"{self.zip_code}, {self.city}"
                f"\nPhone: {self.phone}")


class Book:
    def __init__(self,
                 library: 'Library',
                 publication_date: str,
                 author_name: str,
                 author_surname: str,
                 number_of_pages: int):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (f"Book by {self.author_name} "
                f"{self.author_surname}\nPublication Date: "
                f"{self.publication_date}\nPages: "
                f"{self.number_of_pages}\nLibrary: "
                f"{self.library}")


class Order:
    def __init__(self,
                 employee: 'Employee',
                 student: str,
                 books: list,
                 order_date: str):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = "\n".join(str(book) for book in self.books)
        return (f"Order by "
                f"{self.student}\nEmployee: "
                f"{self.employee}\nOrder Date: "
                f"{self.order_date}\nBooks:\n"
                f"{books_str}")
