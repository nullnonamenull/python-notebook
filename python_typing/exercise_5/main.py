def contains_value(lst: list, value: int) -> bool:
    return value in lst


def main():
    numbers = [1, 3, 5, 7, 9]
    value_to_find = 5
    value_not_in_list = 6

    if contains_value(numbers, value_to_find):
        print(f"{value_to_find} is in the list.")
    else:
        print(f"{value_to_find} is not in the list.")

    if contains_value(numbers, value_not_in_list):
        print(f"{value_not_in_list} is in the list.")
    else:
        print(f"{value_not_in_list} is not in the list.")


if __name__ == "__main__":
    main()
