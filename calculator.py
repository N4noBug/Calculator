# MY calculator 

import random 
import time

def ask_for_numbers(): 
    numbers = input("Enter numbers separated by spaces: ").split()
    return numbers

def add(numbers): 
    results = sum(numbers)
    return results 

def subtract(): 
    pass

def multiply(): 
    pass

def divide(): 
    pass

def modulo(): 
    pass

def exponentiation(): 
    pass

def floor_division(): 
    pass

def square_root(): 
    pass

def percentage(): 
    pass

def absolute_value(): 
    pass

def factorial(): 
    pass

def logarithm(): 
    pass

def trigonometry(): 
    pass    

def random_number(): 
    pass

def temperature_conversion(): 
    pass

def history(): 
    pass

def remove_calculations_from_history(): 
    pass

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
16. History (save and view past calculations)
17. Remove calculations from history
18. Exit

Your choice: """)
        
        if choice == "1": 
            results = add(ask_for_numbers())
            print("Result: ", results)
            time.sleep(3)
        elif choice == "2":
            results = subtract(ask_for_numbers())
            print("Result: ", results)
        elif choice == "3":
            results = multiply(ask_for_numbers())  
            print("Result: ", results)  
        elif choice == "4":
            results = divide(ask_for_numbers())
            print("Result: ", results)
        elif choice == "5":     
            modulo()
        elif choice == "6":
            exponentiation()
        elif choice == "7":
            floor_division()
        elif choice == "8":
            square_root()
        elif choice == "9":
            percentage()
        elif choice == "10":
            absolute_value()
        elif choice == "11":
            factorial()
        elif choice == "12":
            logarithm()
        elif choice == "13":
            trigonometry()
        elif choice == "14":
            random_number()
        elif choice == "15":
            temperature_conversion()
        elif choice == "16":
            history()
        elif choice == "17":
            remove_calculations_from_history()
        elif choice == "18":
            print("Exiting the calculator. Goodbye!")
        else:
            print("Invalid choice. Please select a valid option from the menu.")

if __name__ == "__main__":
    main_program()
