def f(numerator, denominator):
    try:
        numerator = int(numerator)
        denominator = int(denominator)

        result = numerator / denominator
        print(f"The result of the division is: {result}")

    except ValueError:  
        # Handles errors from int() conversion
        print("Invalid input. Please enter only numbers.")
    except ZeroDivisionError:
        # Handles errors from dividing by zero
        print("Error: Cannot divide by zero.")

    print("Program finished.")

f(1, 2)
f('a',2)
f('1',0)