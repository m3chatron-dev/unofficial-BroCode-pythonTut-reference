# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

# THE DICTIONARY
capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# FIND SPECIFIC VALUE
    #print(capitals.get("USA"))

# IF STATEMENT EXAMPLE
    # if capitals.get("Russia"):
        #   print("That capital exists")
    # else:
        #   print("That capital does not exist")

# DIFFERENT COMMANDS
    # capitals.update({"Germany": "Berlin"})
    # capitals.update({"USA": "Detroit"})
    # capitals.pop("China")
    # capitals.popitem()
    # capitals.clear()


# ONLY FIND KEYS
    # keys = capitals.keys()
    # for key in capitals.keys():
    #     print(key)

# ONLY FIND VALUES
    # values = capitals.values()
    # print(values)
    # for value in capitals.values():
        # print(value)

# 2D LIST EXAMPLE
    # items = capitals.items()
    # print(items)
    # for key, value in items:
        # print(f"{key}: {value}")