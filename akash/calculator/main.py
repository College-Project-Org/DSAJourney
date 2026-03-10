from add import add
from sub import sub


def main():
    print("Welcome to the Calculator!")
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Exit")

        choice = input("Enter choice (1/2/3): ")

        if choice == "3":
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ["1", "2"]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = add(num1, num2)
                print(f"The result of addition is: {result}")
            elif choice == "2":
                result = sub(num1, num2)
                print(f"The result of subtraction is: {result}")
        else:
            print("Invalid input. Please enter a valid choice.")


if __name__ == "__main__":
    main()
