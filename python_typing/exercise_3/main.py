def is_even(number: int) -> bool:
    return number % 2 == 0


def main():
    num = int(input("Enter a number: "))

    if is_even(num):
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")


if __name__ == "__main__":
    main()
