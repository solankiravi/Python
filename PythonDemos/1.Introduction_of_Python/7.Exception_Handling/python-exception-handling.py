number1 = 12
number2 = 1
if number1 == number2:
    raise ValueError("Numbers are equal, which is not allowed.")
try:
    result = number1 / number2
except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed.")
except TypeError as e:
    print("Error: Invalid type for division.")
except Exception as e:
    print("An unexpected error occurred:", e)
else:
    print("Result:", result)
finally:
    print("Execution completed.")
