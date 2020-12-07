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



