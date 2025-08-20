def access_list_element(lst, index):
    try:
        element = lst[index]
        print("Element at index", index, ":", element)
    except IndexError:
        print("Error: Index out of range")
my_list = [1, 2, 3, 4, 5]
index = int(input("Enter the index to access: "))
access_list_element(my_list, index)


try:
    num = int(input("Enter an integer: "))
    print("You entered:", num)
except ValueError:
    print("Error: Input could not be converted to an integer")
