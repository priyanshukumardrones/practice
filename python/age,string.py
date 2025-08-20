def concatenate_string_with_integer(name, rollNo):
    try:
        result = name + rollNo
        print("Concatenated string:", result)
    except TypeError:
        print("Error: Cannot concatenate string with integer")
name = "John Doe"
rollNo = 123
concatenate_string_with_integer(name, rollNo)



