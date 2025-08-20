def divide_age_by_zero(age):
    try:
        result = age / 0
        print("Result of dividing age by zero:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
age = 25
divide_age_by_zero(age)
