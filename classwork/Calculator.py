def add(num1: float, num2: float) -> float:
    """ Function to Add Two Numbers"""
    sum = num1 + num2
    return sum


def subtract(num1: float,num2: float) -> float:
    """ Function to Subtract Two Numbers"""
    num3 = num1 - num2
    return num3


def multiply(num1, num2):
    """ Function to Multiply Two Numbers"""
    multiplication = num1 * num2
    return multiplication


def square(num1: float) -> float:
    """ Function accept one args,to calculate the squares"""
    squares = num1 ** 2
    return squares


def square_root(num1):
    """ Function accept one args,to calculate the square root"""
    square_root  = num1 ** 0.5
    return square_root


def divide(num1: float, num2:float) -> float:
    """ Function to Divide Two Numbers"""
    division = num1 / num2
    return division


def main():
    print(add(3, 6))
    print(subtract(4, 3))
    print(divide(9, 3))
    print(multiply(3.9, 3.2))
    print(square(45))
    print(square_root(4))


if __name__ == "__main__":
    main()