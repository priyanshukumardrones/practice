def check(num):
    try:
        if num % 2 == 0:
            result = "1" + str(num)
            print("Concatenated result for even number:", result)
        else:
            result = num / 0
            print("Result of dividing odd number by zero:", result)
    except (TypeError, ZeroDivisionError):
        print("Error: Either TypeError or ZeroDivisionError occurred")
num = 7
check(num)


try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
    print("Result of division:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
except ValueError:
    print("Error: Please enter valid numbers")
