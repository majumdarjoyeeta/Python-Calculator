from art import logo
from colorama import Fore, Style, init

init(autoreset=True)

def calculator_display_menu():
    print(Fore.CYAN + logo)
    print(Fore.GREEN + "\nWelcome to the Python Calculator!")
    print(Fore.YELLOW + "Choose an operation:")
    print(Fore.MAGENTA + "1. Addition (+)")
    print(Fore.MAGENTA + "2. Subtraction (-)")
    print(Fore.MAGENTA + "3. Multiplication (*)")
    print(Fore.MAGENTA + "4. Division (/)")
    print(Fore.MAGENTA + "5. Modulus (%)")
    print(Fore.MAGENTA + "6. Power (^)")
    print(Fore.RED + "7. Exit (q)")

def perform_calculation(choice, a, b):
    if choice == "1":
        return a + b
    elif choice == "2":
        return a - b
    elif choice == "3":
        return a * b
    elif choice == "4":
        return "Error: Division by zero!" if b == 0 else a / b
    elif choice == "5":
        return "Error: Modulus by zero!" if b == 0 else a % b
    elif choice == "6":
        return a ** b

def calculator():
    while True:
        calculator_display_menu()
        choice = input(Fore.CYAN + "Enter your choice (1-6 or '7/q' to quit): ")

        if choice in ["7", "q"]:
            print(Fore.RED + "Goodbye! Thanks for using the Python Calculator.")
            break
        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print(Fore.RED + "Invalid choice. Try again!")
            continue

        try:
            a = float(input(Fore.YELLOW + "Enter the first number: "))
            b = float(input(Fore.YELLOW + "Enter the second number: "))
            result = perform_calculation(choice, a, b)
            print(Fore.GREEN + f"Result: {result}")
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter numbers only!")

        another = input(Fore.CYAN + "Do you want another calculation? (yes/no): ").lower()
        if another != "yes":
            print(Fore.RED + "Goodbye! Thanks for using the Python Calculator.")
            break

calculator()
