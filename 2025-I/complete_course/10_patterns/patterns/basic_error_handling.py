def f(input):
    try:
        user_input = int(input)
        number = int(user_input)
        print(f"You successfully entered the number: {number}")
    except ValueError:
        # This code runs ONLY if a ValueError occurred in the try block
        print("Invalid input. That wasn't a valid number!")

    print("Program finished.") # This line WILL run now, even if input was invalid
f(1)