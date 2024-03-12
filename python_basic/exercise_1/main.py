def print_names(names_list):
    for name in names_list:
        print(name)


def double_numbers_loop(numbers_list):
    doubled_list = []
    for number in numbers_list:
        doubled_list.append(number * 2)
    return doubled_list


def double_numbers_comprehension(numbers_list):
    return [number * 2 for number in numbers_list]


def print_even_numbers(numbers_list):
    for number in numbers_list:
        if number % 2 == 0:
            print(number)


def display_even_numbers(numbers_list):
    even_numbers = [number for number in numbers_list if number % 2 == 0]
    print("Even numbers:", even_numbers)


def main():
    names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    numbers = [1, 2, 3, 4, 5]
    numbers_10 = range(1, 11)

    print("Print Names:")
    print_names(names)
    print("\nDouble Numbers (Loop):")
    print(double_numbers_loop(numbers))
    print("\nDouble Numbers (Comprehension):")
    print(double_numbers_comprehension(numbers))
    print("\nPrint Even Numbers:")
    print_even_numbers(numbers_10)
    print("\nDisplay Even Numbers:")
    display_even_numbers(numbers_10)


if __name__ == "__main__":
    main()
