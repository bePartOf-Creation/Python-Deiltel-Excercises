first_num = 10
second_num = 20
if first_num > second_num:
    print("The first number is the largest")
else:
    print("The second number is the largest")
    ##
    for i in range(10):
        print(i)
# To Selection , u need a collection
kel = "hello"
kelly_family = ['fortune','deer','jane']
for i,j in enumerate (kel):
    print(i,j)
for i, j in enumerate(kel):
    print(kel)
for i, j in enumerate(kel, start= 1):
    print(i,j)
for i in range(20,0,-2):
    print(i)
#Defining A function.
def c2f(celcius):
        result = (celcius * 1.8) + 32
        print(result)
new_temperature = c2f(20)
