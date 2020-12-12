# for loop - is a way to iterate through a collection in Python. It is called 'for' loop because we use it to do
# something for each element in a collection.

# Iterate through a collection - convention to use i to stand in as a variable
n = 10
for i in range(n):
    print(i)
# function  called range = list of numbers from 0 up to and inc n???????? -
# error in lesson possible here (don't think it includes the value n).
# To do something 100 times you would write range(100)

for i in range(100):
    if i%5==0:
        print(i)
# in this case %5 = modulus 5 or "get the remainder of dividing by 5"
# so i%5 == 0 means if you divide i by 5 you don't get remainder

print('i','i//5','i%5',sep='\t')
# 'sep' means separate the elements using the
# '\t' which in this case is a tab character.

for i in range(100):
    print(i, i//5, i%5, sep='\t')
# i//5 is showing i//5 with no remainder, remainder is displayed by i%5
# therefore column b*5 + c = a
# can cross check with final table value as shown below:
print((19*5)+4)

# again showing how we might only want to print value if condition is met e.g:
for i in range(100):
    if i%5==0:
        print(i)

# Above section shows you to iterate ranges - now we move on to iterative strings

list_of_stings = ['apple', 'banana', 'cherry', 'date']
for i in list_of_stings:
    print(i)

# if we iterate through a string, we will iterate through each character in turn
# iterating through a set and then within that set is called a 'double loop'
# Double loops allow for iteration in 2 dimensions

# Also importing time - google online to find out more details about what this adds
# in this case it gets 1 char in each word every second. 0.1 would be every 0.1 s --- play with the speed here

import time
list_of_strings = ['apple', 'banana', 'cherry', 'date']
for word in list_of_strings:
    for char in word:
        print(char, end='_')
        time.sleep(0.001)
    print()
# move print function through the loops to see effect on chars printed
# didn't have to use word and char here but it helps to understand code for this example
# end='_' is inputted as leaving it out gives standard \n which looks messy!

import time
raw_scores = [[30, 18, 25, 25],
              [20, 28, 17, 22],
              [21, 22, 24, 18]]
print(raw_scores)

for row in raw_scores:
    for mark in row:
        print(mark, end=', ')
        time.sleep(0.2)
    print()
print()
for row in raw_scores:
    for mark in row:
        print('{:.0f}%'.format((mark/30)*100), end=', ')
        time.sleep(0.02)
    print()
list_of_strings = ["apple", 'banana', 'cherry', 'date']*3
counter = 0
for i in list_of_strings:
    print((counter), i.title(), sep='\t\t')
    counter += 1
# We put counter at the bottom because we want the first index to equal 0
# See below for counter before print statement - first index is labelled 1 even though it is 0


list_of_strings = ["apple", 'banana', 'cherry', 'date']*3
counter = 0
for i in list_of_strings:
    counter += 1
    print((counter), i.title(), sep='\t\t')

#  Enumerate method
# This function takes in your collection and then during the 'for' loop
# returns both a counter and one element at a time from your collection

list_of_strings = ["apple", 'banana', 'cherry', 'date']
for counter, element in enumerate(list_of_strings):
    print(counter, element.title(), sep='. ')

# Instead of a counter, it is common to see people using just the letter 'c'. Then when you want to report
# something every tenth or thousandth time the loop runs you would insert in your code:

# if c%1000 == 0:
#     print('Line %s' % c)

list_of_strings = ["apple", 'banana', 'cherry', 'date']
for counter, element in enumerate(list_of_strings):
    if counter %2 == 0:
        print(counter, element.title(), sep='. ')


# Iterating Dictionaries
# how iteration works with key:value pairs or 'items'

ingredients = {'salt':'parmesean',
               'fat':'olive oil',
               'acid':'vinegar',
               'heat':'toast'
               }
# method here is - quality:food - helps understand for loop names below
print(ingredients.items(), end='\n\n')
for quality, food in ingredients.items():
    print(quality, food, sep='--->')

# methods of dictionary print below:

food_dict = {'fish':'salmon',
             'mushroom':'enoki',
             'fruit':'apple',
             'vegetable':'potato'
             }
for key in food_dict.keys():
    print(key)

for value in food_dict.values():
    print(value)

for item in food_dict.items():
    print(item)

# Notice in the print here you get what looks like a list - this is called a Tuple
# Tuple is a list except its immutable (can't change it) and has parenthesis '()' instead of brackets '[]'

# So with a list you could go my_list[2] = 'normal' and it would replace third index with normal.
# with a tuple you cannot, you can query it with my_tuple[2]

my_list = ['ant', 'ladybug', 'beetle']
print(my_list[2])
my_list[2] = 'grasshopper'
print(my_list[2])

my_tuple = ('ant', 'ladybug', 'beetle')
print(my_tuple[2])
# my_tuple[2] = 'grasshopper'
# print(my_tuple[2])

# commented out to remove error in run window
# notice how here square brackets still applies when printing indexes of a tuple.

# Iterating a table of values

for row in range(5):
    for column in range(5):
        print(row, end=' ')
    print()

for row in range(5):
    for column in range(5):
        print(column, end=' ')
    print('\n')

for row in range(5):
    for col in range(5):
        print(row+col, end=' ')
    print()

for row in range(10):
    for col in range(10):
        if (row+col)%2==0:
            print('x', end=' ')
        else:
            print('o', end=' ')
    print()

word = "point"
for i in range(len(word)):
        print(word[:i+1], sep='')

word = "point"
for i in range(len(word)):
    print(word[i:], sep='')



word = "point"
for i in range(len(word)):
    print(word[i:], word[:i], sep='')


# CLARIFYING CONTINUE, PASS AND BREAK

for j in range(10):
    if j <=5:
        print(j)
    else:
        break
    print('Hello')

for j in range(10):
    if j<5:
        print(j)
    else:
        pass
    print('Higher')
    

# print("Leave by throwing an error")
#
# for a in range(0, 100, 25):
#     print(f"Value: {a}\t value / (value-75): {a/(a-75)}")
#
# print("Hi, it's the end!")


# Breaking inner loop vs breaking outer loop

print("Now with a break statement", end="\n\n")
for i in range(5):
    for j in range(100,105):
        if j%3 == 0:
            break
        print(f"outer loop {i}: inner loop {j}")
    print()

print("Now with a break statement", end="\n\n")
for i in range(5):
    for j in range(100,105):
        if i%3 == 0:
            break
        print(f"outer loop {i}: inner loop {j}")
    print()
# continue - goes to next element in them loop, break will stop the loop

print("Now with a break statement", end="\n\n")
for i in range(5):
    for j in range(100,105):
        if j%3 == 0:
            continue
        print(f"outer loop {i}: inner loop {j}")
    print()


# Conditionals and more loops

x = 4
y = 5
z = 5

print(x == y)
print(y == z)
print(x == z)

print(not(x == y))
ex_list = [1,3,5]
print(z in ex_list)

x = 5
y = 3
z = x + y

if z == 7:
    print("Yes, Z equals 7.")
else:
    print("My maths is not good today :(")

# Introducing nested statements with elif which is a contraction of else if

x = 5
y = 5
z = x + y

if z == 10:
    print("Hmm... should this be? ")
elif z == 7:
    print("Okay, I was worried for a second there.")
else:
    print("I give up.")


# 0 is false, 1 is true, other numbers are nor true or false

# when importing libraries - you can see the statement below to "import as" which makes it so you dont have
# to write the full word out. e.g. rather than import numpy --- you can import numpy as np
# VERY COMMON

food_list = ["apple", 'banana', 'chocolate', 'dumpling']

counter = 0
for i in food_list:
    print('Food number', counter, "is", i)
    counter += 1

print()
# Shows how to enumerate to do something every nth time.
for c, i in enumerate(food_list):
    print("Food number", c, "is", i)

# Shows building a new changed string and then printing the edited string

example_str = "Print every third character of this line as upper case"
outstr = ""

for c, i in enumerate(example_str):
    if c%3 == 0:
        outstr += i.upper()
    else:
        outstr += i
print(outstr)

example_str = "Print every third character of this line as upper case"
newstr = "asdasdasdasdada -----"

for c,i in enumerate(example_str):
    if c%3 == 0:
        newstr += i.upper()
    else:
        newstr += i

print(newstr)

for i in range(100):
    if i%25 == 0:
        print(i)

# List Comprehensions


# This is an example of a normal 'non-pythonic' method
my_list = ["allspice", "basil", "cumin"]

new_list = []
for i in my_list:
    i = i.upper()
    new_list.append(i)

print(new_list)

# List comp method:

my_list = ["allspice", "basil", "cumin"]
new_list = [i.upper() for i in my_list]
print(new_list)

my_list = ["allspice", "basil", "cumin"]
new_list = [i.upper()*2 for i in my_list]
print(new_list)


# Slightly more advanced list comprehension

my_list = ["allspice", "basil", "cumin"]
new_list = []
for i in my_list:
    if len(i) == 5:
        i = i.title()
        new_list.append(i)
print(new_list)

new_list = [i.title() for i in my_list if len(i) == 5]
print(new_list)

# Dictionary Comprehensions

my_dict = {1:'allspice', 2:'Basil', 3:'cumin'}

new_dict = {key: value.title() for key, value in my_dict.items() if len(value) == 5}
print(new_dict)

import random as rd

print(rd.randint(0,10))

x = True

while x:
    random_number = rd.randint(0, 50)
    print(random_number)

    if random_number == 1:              # DON'T COMMENT THIS OUT OR YOU GET INFINITE LOOP!!
        x = False

