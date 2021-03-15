def check_vowels(word):
    contains = False
    for i in word:
        word_lower = i.lower()
        if word_lower in ['a', 'e', 'i', 'o', 'u']:
            contains = True
            break
    if contains:
        print("String contain a vowel")
    else:
        print("Does not contain a vowel")


def main():
    user_input = input("Enter a String")
    check_vowels(user_input)


if __name__ == '__main__':
    main()
