def multiply(a: int, b: int) -> int:
    return a * b


def main():
    num_one = int(input("Enter first integer: "))
    num_two = int(input("Enter second integer: "))

    result = multiply(num_one, num_two)
    print(f"The multiplication of {num_one} and {num_two} is {result}.")


if __name__ == "__main__":
    main()
