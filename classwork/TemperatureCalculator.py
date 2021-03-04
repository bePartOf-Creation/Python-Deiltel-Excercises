from classwork.utils import *


def temperature(celcius):
    result = multiply(celcius, 1.8)
    return add(result, 32)


def main():
    user_input = int(input("Input Convert To Fahrenheit: \n"))
    print(temperature(user_input))
    print(all_temperature())


if __name__ == "__main__":
    main()

