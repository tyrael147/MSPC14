def f(number):
    try:
        number = int(number)
    except ValueError:
        print("Invalid input. That wasn't a valid number!")
    else:
        # This runs ONLY if the try block succeeded without errors
        print(f"You successfully entered the number: {number}")
        # Maybe perform further calculations with 'number' here

    print("Program finished.")

f(1)
f('a')