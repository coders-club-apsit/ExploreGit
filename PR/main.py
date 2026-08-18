from arithmetic import add, subtract, multiply, divide


def main():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Choose an operation: ")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", add(a, b))

    elif choice == "2":
        print("Result:", subtract(a, b))

    elif choice == "3":
        print("Result:", multiply(a, b))

    elif choice == "4":
        print("Result:", divide(a, b))

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()