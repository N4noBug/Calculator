# MY calculator 

import random 

history_list = []

# INPUT
def ask_for_numbers(): 
    while True: 
        try: 
            numbers = input("Enter numbers separated by spaces: ").split()
            return list(map(float,numbers))
        except ValueError: 
            print("Invalid input. Please enter numbers only.")

# OPERATIONS
def add(numbers): 
    result = sum(numbers)
    history_list.append(f"Add: {numbers} = {result}")
    return result

def subtract(numbers): 
    result  = numbers[0]
    for n in numbers[1:]: 
        result -= n 
    history_list.append(f"Subtract: {numbers} = {result}")
    return result 

def multiply(numbers): 
    result = 1
    for n in numbers: 
        result *= n 
    history_list.append(f"Multiply: {numbers} = {result}")
    return result

def divide(numbers): 
    result = numbers[0]
    for n in numbers[1:]:
        if n == 0: 
            history_list.append(f"Divide ERROR: {numbers} (division by zero)")
            return "Error: Cannot divide by zero"
        result /= n 
    history_list.append(f"Divide: {numbers} = {result}")
    return result
    
def modulo(numbers): 
    result = numbers[0]
    for n in numbers[1:]:
        if n == 0:
            history_list.append(f"Modulo ERROR: {numbers} (division by zero)")
            return "Error: Cannot divide by zero"
        result %= n 
    history_list.append(f"Modulo: {numbers} = {result}")
    return result

def exponentiation(numbers): 
    result = numbers[0]
    for n in numbers[1:]:
        result **= n 
    history_list.append(f"Exponentiation: {numbers} = {result}")
    return result

def floor_division(numbers): 
    result = numbers[0]
    for n in numbers[1:]: 
        if n == 0: 
            return "Cannot divide by zero"
        result //= n 
    history_list.append(f"Floor Division: {numbers} = {result}")
    return result

def square_root(numbers): 
    if numbers[0] < 0: 
        return "Cannot take square root of a negative number"
    result = numbers[0]**0.5
    history_list.append(f"Square Root: {numbers[0]} = {result}")
    return result
    
def percentage(numbers): 
    result = (numbers[0] / 100) * numbers[1]
    history_list.append(f"Percentage: {numbers} = {result}")
    return result

def absolute_value(numbers): 
    result = -numbers[0] if numbers[0] < 0 else numbers[0]
    history_list.append(f"Absolute Value: {numbers[0]} = {result}")
    return result

def factorial(numbers): 
    n = int(numbers[0])
    if n < 0: 
        return "Cannot factorial negative numbers"
    if n != int(n): 
        return "Factorial only works with whole numbers"
    n = int(n)
    result = 1
    for i in range(1,n+1): 
        result *= i
    history_list.append(f"Factorial: {n} = {result}")
    return result

def logarithm(numbers): 
    x = numbers[0]
    if x <= 0:
        return "Cannot calculate logarithm of non-positive number"
    result = 0 
    while x > 1: 
        x /= 10 
        result += 1 
    history_list.append(f"Log10 approx: {numbers[0]} = {result}")
    return result

def trigonometry(numbers): 
    x = numbers[0]
    result = x - (x**3)/6 + (x**5)/120 
    history_list.append(f"Trigonometry: {numbers[0]} = {result}")  
    return result      

def random_number(): 
    result = random.randint(1,100)
    history_list.append(f"Random Number: {result}")
    return result

def temperature_conversion(numbers): 
    c = numbers[0]
    f = (c*9/5) + 32
    history_list.append(f"Temperature Conversion: {c}C = {f}F")
    return f

def history(): 
    print(f"\n --- HISTORY ---")
    for item in history_list: 
        print(item)

def remove_calculations_from_history(): 
    history_list.clear()
    print("History cleared!")

def pause(): 
    input("\nPress Enter to go back to menu...")

# MAIN PROGRAM
def main_program(): 
    while True: 
        choice = input("""
What do you want to do? 

1. Add
2. Subtract
3. Multiply
4. Divide
5. Modulo
6. Exponentiation
7. Floor Division
8. Square Root
9. Percentage
10. Absolute Value
11. Factorial
12. Logarithm
13. Trigonometry
14. Random Number
15. Temperature Conversion
16. View History
17. Remove History 
18. Exit

Your choice: """)

        if choice == "1": 
            print("Result: ", add(ask_for_numbers()))
            pause()
        elif choice == "2":
            print("Result: ", subtract(ask_for_numbers()))
            pause()
        elif choice == "3":
            print("Result: ", multiply(ask_for_numbers()))
            pause()
        elif choice == "4":
            print("Result: ", divide(ask_for_numbers()))
            pause()
        elif choice == "5":     
            print("Result: ", modulo(ask_for_numbers()))
            pause()
        elif choice == "6":
            print("Result: ", exponentiation(ask_for_numbers()))
            pause()
        elif choice == "7":
            print("Result: ", floor_division(ask_for_numbers()))
            pause()
        elif choice == "8":
            print("Result: ", square_root(ask_for_numbers()))
            pause()
        elif choice == "9":
            print("Result: ", percentage(ask_for_numbers()))
            pause()
        elif choice == "10":
            print("Result: ", absolute_value(ask_for_numbers()))
            pause()
        elif choice == "11":
            print("Result: ", factorial(ask_for_numbers()))
            pause()
        elif choice == "12":
            print("Result: ", logarithm(ask_for_numbers()))
            pause()
        elif choice == "13":
            print("Result: ", trigonometry(ask_for_numbers()))
            pause()
        elif choice == "14":
            print("Result: ", random_number())
            pause()
        elif choice == "15":
            print("Result: ", temperature_conversion(ask_for_numbers()))
            pause()
        elif choice == "16":
            history()
            pause()
        elif choice == "17": 
            remove_calculations_from_history()
            pause()
        elif choice == "18":
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option from the menu.")
            pause()

if __name__ == "__main__":
    main_program()
