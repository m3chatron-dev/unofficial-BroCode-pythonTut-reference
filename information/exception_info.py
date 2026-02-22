# exception = An event that interrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#             1. try, 2. excerpt, 3. finally

try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divide by zero IDIOT!")
except ValueError:
    print("Enter only numbers please!")
except Exception:
    print("Something went wrong!")
finally:
    print("Do some cleanup here")

# theoretically you could only use this to get all exceptions in one line:
"""
except Exception:
    print("Something went wrong!")
"""
# however, this is inefficient and would only give one message, not explaining any specific errors