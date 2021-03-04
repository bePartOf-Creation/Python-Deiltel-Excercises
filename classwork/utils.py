def add(num1: float, num2: float) -> float:
    num3 = num1 + num2
    return num3


def multiply(num1: float, num2: float) -> float:
    multiplication = num1 * num2
    return multiplication


def temperature(celcius):
    result = multiply(celcius, 1.8)
    return add(result, 32)


def all_temperature():
    user_input = input("Enter all Temperature values: \n")   # To accept Multiple Inputs
    user_input_list = user_input.split(",")   # Split the Numbers by commas(,)

    print(user_input_list)   # Display the lists
    for i in user_input_list:  # "i" represent each number entered in the user_input_list, pick it
        result = temperature(float(i))  #
        print(result)


def main():
    """Function call"""
    print(add(2, 4))
    print(multiply(7, 1))
    all_temperature()


if __name__ == "__main__":
    main()
