def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    # Logical Error: Incorrect average calculation for empty list
    return total / len(numbers)

data1 = [10, 20, 30, 40, 50]
data2 = [5, 15]
data3 = [] # This will cause an error
print(f"Average of data1: {calculate_average(data1)}")
print(f"Average of data2: {calculate_average(data2)}")
print(f"Average of data3: {calculate_average(data3)}")
def calculate_average(numbers):
    """
    Returns the average of a list of numbers.
    Returns None if the list is empty.
    """
    try:
        total = 0
        for num in numbers:
            total += num
        return total / len(numbers)
    except ZeroDivisionError:
        return None
def get_list_element(my_list, index):
    """
    Returns the element at the given index.
    Handles IndexError and TypeError.
    """
    try:
        return my_list[index]
    except IndexError:
        print("Error: Index is out of bounds.")
        return None
    except TypeError:
        print("Error: Provided input is not a list.")
        return None
    print(f"Average of data1: {calculate_average(data1)}")
print(f"Average of data2: {calculate_average(data2)}")
print(f"Average of data3: {calculate_average(data3)}")

# get_list_element examples
print(get_list_element([1, 2, 3], 1))       # Valid
print(get_list_element([1, 2, 3], 10))      # Out of bounds
print(get_list_element("not a list", 1))    # Incorrect type