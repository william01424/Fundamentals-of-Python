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

