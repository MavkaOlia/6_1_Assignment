def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def main():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")

    choice = input("Enter choice (1, 2 or 3): ")

    if choice not in ('1', '2', '3'):
        print("Invalid choice. Exiting.")
        return

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = add(num1, num2)
        print(f"Result: {num1} + {num2} = {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"Result: {num1} - {num2} = {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"Result: {num1} * {num2} = {result}")

if __name__ == "__main__":
    main()
