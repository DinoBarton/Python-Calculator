def add(numbers):
    return sum(numbers)
def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def divide(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num != 0:
            result /= num
        else:
            print("Error: Cannot divide by zero.")
            return None
    return result

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

print("Welcome to the Advanced Calculator!")

while True:
    print("\nSelect an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Divide")
    print("4. Calculate Average")
    print("5. Exit")

    choice = input("Enter the number of your choice: ")

    if choice == '5':
        print("Goodbye!")
        break

    numbers = []
    num_count = int(input("Enter the number of values: "))
    for i in range(num_count):
        num = float(input(f"Enter value {i + 1}: "))
        numbers.append(num)

    if choice == '1':
        print("Result:", add(numbers))
    elif choice == '2':
        print("Result:", subtract(numbers))
    elif choice == '3':
        print("Result:", divide(numbers))
    elif choice == '4':
        print("Average:", calculate_average(numbers))
    else:
        print("Invalid choice. Please select a valid operation.")
