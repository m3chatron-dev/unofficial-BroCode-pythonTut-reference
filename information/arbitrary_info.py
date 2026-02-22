# *args    = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#            * unpacking operator
#            1. positional 2. default 3. keyword 4. ARBITRARY

# NOTE: "*args" AND "**kwargs" CAN HAVE THEIR NAME CHANGED, ONLY THE APOSTROPHES MATTER

# *args | type: Tuple
    # def display_name(*args):
        # for arg in args:
            # print(arg, end=" ")

    # display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")

# **kwargs | type: Dictionary
    # def print_address(**kwargs):
        # for  key, value in kwargs.items():
            # print(f"{key}: {value}")

    # print_address(street = "123 Fake St.",
                  # apt = "100",
                  # city = "Detroit",
                  # state = "MI",
                  # zip = "54321")

# USING BOTH

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end = " ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street="123 Fake St.",
#              apt = "#100",
#              pobox = "PO Box #1001",
               city = "Detroit",
               state = "MI",
               zip = "54321")