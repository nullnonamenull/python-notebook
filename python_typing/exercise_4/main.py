def is_sum_greater_or_equal(a: int, b: int, c: int) -> bool:
    return (a + b) >= c


def main():
    num1 = int(input("Enter first integer: "))
    num2 = int(input("Enter second integer: "))
    num3 = int(input("Enter third integer: "))

    if is_sum_greater_or_equal(num1, num2, num3):
        print("The sum of the first two numbers is "
              "greater than or equal to the third number.")
    else:
        print("The sum of the first two numbers "
              "is less than the third number.")


if __name__ == "__main__":
    main()
