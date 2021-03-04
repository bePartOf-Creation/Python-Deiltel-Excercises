from classwork.Calculator import *


def run_test():
    assert add(2, 2) == 4, "2 + 2 is 4"
    assert subtract(7, 3) == 4, "7 - 3 is 5"
    assert multiply(2, 3) == 6, "2 * 3 is 6"
    assert divide(14, 2) == 7, "14 + 2 is 7"
    assert square_root(64) == 8, "Square of 64 is 8"
    assert square(3) == 9,  "Squares of 3 is 9"


if __name__ == "__main__":
   main()