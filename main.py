# 2.1 (What does this code do?) Create the variables x = 2 and y = 3, then determine what
# each of the following statements displays:
# a) print('x =', x)
# b) print('Value of', x, '+', x, 'is', (x + x))
# c) print('x =')
# d) print((x + y), '=', (y + x))
x = 2
y = 3
print('x = ', 2)
print('Value of', x, '+', x, 'is', (x + x))
print('x =')
print((x + y), '=', (y + x))


# (Fill in the missing code) Replace *** in the following code with a statement that
# will print a message like 'Congratulations! Your grade of 91 earns you an A in this
# course'. Your statement should print the value stored in the variable grade:
# if grade >= 90:
#  ***

grade =int(input('Enter grade : '))
if grade >= 90:
    print('Congratulations! Your grade of  91 earns you an A in this course')
else:
    print('failure')

# (Arithmetic) For each of the arithmetic operators +, -, *, /, // and **, display the
# value of an expression with 27.5 as the left operand and 2 as the right operand.
x = 27.5
y = 2
print('Value of ', x, 'and', y, 'is =', (x+y))
print('Value of ', x, 'and', y, 'is =', (x-y))
print('Value of ', x, 'and', y, 'is =', (x*y))
print('Value of ', x, 'and', y, 'is =', (x/y))
print('Value of ', x, 'and', y, 'is =', (x//y))
print('Value of ', x, 'and', y, 'is =', (x**y))
# (Circle Area, Diameter and Circumference) For a circle of radius 2, display the diameter, circumference and area. Use the value
# 3.14159 for π. Use the following formulas
# (r is the radius): diameter = 2r, circumference = 2πr and area = πr2. [In a later chapter, we’ll
# introduce Python’s math module which contains a higher-precision representation of π.]
radius = 2
π = 3.1459
print('Value of Diameter', 'is =', (2*radius))
print('Value of Circumference', 'is =', (2 * π * radius))
print('Value of Area','is',(π * radius * radius))
# (Odd or Even) Use if statements to determine whether an integer is odd or even.
# [Hint: Use the remainder operator. An even number is a multiple of 2. Any multiple of 2
# leaves a remainder of 0 when divided by 2.]
number = int(input('Enter your number: '))
if number % 2 == 0:
    print(number,'is Even')
elif number % 2 == 1:
    print(number, 'is Odd')


# (Multiples) Use if statements to determine whether 1024 is a multiple of 4 and
# whether 2 is a multiple of 10. (Hint: Use the remainder operator.)
number = int(input('Enter your number: '))
if number % 4 == 0:
    print(number,'is a Multiples of 4')
elif number % 4 == 1:
    print(number,'is not a Multiple of 4')

number2 = int(input('Enter your number: '))
if number2 % 2 == 0:
    print(number2, 'is a Multiple of 2')
elif number2 % 2 == 1:
    print(number2, 'is a not a Multiple of 2')
else:
    print(number,'and',number2,'is not a Multiples of either 4 and 2')


