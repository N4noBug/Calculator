# MY calculator 

choice = input("""What do you want to do? 
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
""")

add(numbers): 
    return sum(numbers)
    

subtract()

multiply()

divide()

modulo()

exponentiation()

floor_division()

square_root()

percentage()

absolute_value()

factorial()

logarithm()

trigonometry()

random_number()

temperature_conversion()

history()

remove_calculations_from_history()

ask_for_numbers(): 
    numbers = input("Enter how many numbers you want to calculate with: ")
    return list(map(float, input("Enter the numbers separated by space: ").split()))    

main_program(choice)
if choice == "1": 
    results = add(ask_for_numbers())
    print("Result: ", results)
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
