num = [1,2,5,4,3] # declare a list
# function that can be performed on a list
print(num)
num.append(78) # To add
print(num)
num.extend([2,3,3,4]) #To  add more than one value.
print(num)
num.insert(0,99) # To insert an value with to desired index-value in a list.
print(num)
num.remove(78) # To remove a value in a list. remove accepts a value in the list as an args
print(num)
num.pop(2)
print(num)
num[0] += 1 # To add 0ne to first Index value or Update
print(num)
num += [6,23] # To add another value without using append(). or concatenate two or more list
print(num)
# Differentiating a tuple `
describe = (1) # int
describer = (1,) # tuple
type(describe)
print(type(describer))
num.pop(2) # Pop accepts an index-value not a value, so 2 is an index in my list
print(num)
# Differentiating a tuple
describe = [1] # LIst
describer = [1,] # List
type(describe)
print(type(describer))
# Differentiating a set
describe = {1} # set
describer = {1,} # set
type(describe)
print(type(describer))

Hello_str ='hello world'

print(Hello_str[3:-2])

# to use "implode function" , you have to create declare a string or lists of strings[A collection]
names =["Remi","Tade","Dele"]
print(names)
names_joined = "-".join(names)
print(names_joined)
names_joined = "*".join(names)
print(names_joined)
names_joined = "+".join(names)
print(names_joined)