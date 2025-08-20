def concatenate_arguments(arg1, arg2):
    try:
        result = str(arg1) + str(arg2)
        print("Concatenated result:", result)
    except TypeError:
        print("Error: One of the arguments is not a string")
arg1 = "Hello"
arg2 = 123
concatenate_arguments(arg1, arg2)
