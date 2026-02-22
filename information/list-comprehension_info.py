# List comprehension = A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

# NUMBER EXAMPLES
    # doubles = [x * 2 for x in range(1, 11)]
    # triples = [y * 3 for y in range(1, 11)]
    # squares = [z * z for z in range(1, 11)]

    # print(doubles)
    # print(triples)
    # print(squares)

# FRUIT EXAMPLE
    # fruits = ["apple", "orange", "banana", "coconut"]
    # fruits = [fruit.upper() for fruit in fruits]
    # fruit_chars = [fruit[0] for fruit in fruits]
    # print(fruits)
    # print(fruit_chars)

# COMPARISON EXAMPLES
    # numbers = [1, -2, 3, -4, 5, -6, 8, -7]
    # positive_nums = [num for num in numbers if num >= 0]
    # negative_nums = [num for num in numbers if num < 0]
    # even_nums = [num for num in numbers if num % 2 == 0]
    # odd_nums = [num for num in numbers if num % 2 == 1]


    # print(numbers)
    # print(positive_nums)
    # print(negative_nums)
    # print(even_nums)
    # print(odd_nums)

# GRADE EXAMPLE
    # grades = [85, 42, 79, 90, 56, 61, 30]
    # passing_grades = [grade for grade in grades if grade >= 60]
    # print(passing_grades)