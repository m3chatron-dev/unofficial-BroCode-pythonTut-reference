
# | LIST [] | (ordered and changeable, duplicates ok)

    # fruits = ["apple", "orange", "banana", "coconut"]

    # print(dir(fruits))
    # print(help(fruits))
    # print(len(fruits))
    # print("apple" in fruits)

    # fruits[0] = "pineapple"
    # fruits.append("pineapple")
    # fruits.remove("apple")
    # fruits.insert(0, "pineapple")

    # | Use both lines to sort in alphabetical order in reverse
    # fruits.sort()
    # fruits.reverse()

    # fruits.clear()
    # print(fruits.index("apple"))
    # print(fruits.count("banana"))

    # print(fruits)
    #for fruit in fruits:
        #print(fruit)

# | SET {} | (random order and cannot be changed including no duplications, but add/remove ok)

    # fruits = {"apple", "orange", "banana", "coconut", "coconut"} # <<< only 1 'coconut'
    # for fruit in fruits:
        # print(fruit)
    # print(dir(fruits))
    # print(help(fruits))

    # print("pineapple in fruits")
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ Syntax (sets are in random order)

    # fruits.add("pineapple")
    # fruits.remove("apple")
    # fruits.pop()
    # fruits.clear()
    # print(fruits)

# | TUPLE () | (ordered and unchangeable, but duplicates ok, FASTER)

    # fruits = {"apple", "orange", "banana", "coconut", "coconut"}
    # print(dir(fruits))
    # print(help(fruits))

    # print(fruits.index("apple"))
    # print(fruits.count("coconut"))
    #for fruit in fruits:
        #print(fruit)