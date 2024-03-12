def combine_lists(lst1: list, lst2: list) -> list:
    combined = lst1 + lst2
    unique = list(set(combined))
    cubed = [x ** 3 for x in unique]
    return cubed


def main():
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]

    result = combine_lists(list1, list2)
    print(result)


if __name__ == "__main__":
    main()
