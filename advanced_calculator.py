import math

def power(base, exponent):
    return base ** exponent

def square_root(x):
    if x < 0:
        return "Square root of negative number is not allowed."
    return math.sqrt(x)

if __name__ == "__main__":
    print("Advanced Calculator")
    print("Select operation:")
    print("1. Power (x^y)")
    print("2. Square Root")

    choice = input("Enter choice (1/2): ")

    if choice == '1':
        base = float(input("Enter base number: "))
        exponent = float(input("Enter exponent: "))
        print("Result:", power(base, exponent))
    elif choice == '2':
        number = float(input("Enter a number: "))
        print("Result:", square_root(number))
    else:
        print("Invalid input")
