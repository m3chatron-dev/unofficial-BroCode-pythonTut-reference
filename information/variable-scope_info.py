# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in


# LOCAL VARIABLE
    # def func1():
    #     x = 1
    #     print(x)

    # def func2():
    #     x = 2
    #     print(x)


# ENCLOSED FUNCTION/VARIABLE
    # def func1():
    #     x = 1

    #     def func2():
    #         print(x)
    #     func2()

    # func1()


# GLOBAL VARIABLE

# x = 3 <---- Can't be before the functions because they will redefine it locally

# def func1():
#      x = 1
#      print(x)

# def func2():
#      x = 2
#      print(x)

# x = 3 <---- Perfect spot

# func1()
# func2()

# x = 3 <---- Can't be after the functions have been invoked because it will use the definition it has from previous lines


# BUILT-IN VARIABLES

    # from math import e

    # def func1():
    #     print(e)

    # e = 3 <---- You cannot redefine it in the middle of the import and the func1() lines because it will interfere with its intended use

    # func1()