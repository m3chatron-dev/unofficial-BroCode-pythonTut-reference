
#The * in the next line means everything
# from script2 import *

# print(__name__)

def favorite_food(food):
    print(f"Your favorite food is {food}")

def main():
    print("This is script1")
    favorite_food("pizza")
    print("Goodbye!")

if __name__ == '__main__':
    main()