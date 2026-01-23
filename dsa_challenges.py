def filter_and_sort_evens(numbers):
    evens = []

    for num in numbers:
        if num % 2 == 0:
            evens.append(num)

    evens.sort()
    return evens


numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = filter_and_sort_evens(numbers)
print(result)

def count_character_frequency(text):
    frequency = {}

    text = text.lower()

    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency


text = "Hello World"
result = count_character_frequency(text)
print(result)