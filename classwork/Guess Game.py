import random

user_input = input("Guess A number To win this Game: ")


def guess(num):
    try:
        number = int(num)
        while number != -1:
            random_number = random.randint(1, 10)
            print(random_number)
            if number == random_number:
                print("Stop!!!  You Guessed Right!")
                break
            else:
                number = int(input("Guess Again..You Can do Better: "))
    except ValueError:
        print("Oga Get SENSE NOW...ENTER A NUMBER IDIOT...")


def main():
    guess(user_input)


if __name__ == '__main__':
    main()
