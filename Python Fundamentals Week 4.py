# Fundamentals of Python Week 4
# Errors Functions, Classes, 'Free' Coding

# Error Handling - ways to make code more 'robust'
# Functions - make our code more modular or reusable
# Classes - more structured code

# 1/0
# How do we catch this basic error - see try and except in the example below

import numpy as np

for i in range(-5, 5):
    try:
        print(1/i)
    except ZeroDivisionError: # This doesn't stop the program when this error fires, it just prints nan instead
        print(np.nan)


# The following code pattern will allow us to reveal what a specific error is. (i.e. we might not know that
# ZeroDivisionError is division by zero. - Therefore we can use the following code to get a readable definition.

try:
    1/0
except Exception as err:     # 'err' is variable name it can be anything.
    print(err)
    print(type(err).__name__)


# Raising your own errors in complex programs

# x = 4
#
# if int(x):
#     raise TypeError('We did not want that number.') # When we get int(x) then we get our error


# Functions

list_result =[]

x = 5
if x %2 == 1:   list_result.append(x*2)
else:           list_result.append(x)

x = 7
if x %2 == 1:   list_result.append(x*2)
else:           list_result.append(x)

x = 12
if x %2 == 1:   list_result.append(x*2)
else:           list_result.append(x)

print(list_result)

def doubleifodd(num):
    if num % 2 == 1: return (num * 2)
    else: return(num)

print([doubleifodd(x) for x in list_result])

# To build a function we need a name, inputs, calculations, and outputs.
# Functions have local variables - outside functions, variables are global.

# You can't call the input of a function outside of the function - see below:

# x = 6
# # print('Before the function', input_number)
# def DoubleValue(input_number):
#     a = input_number * 2
#     print('Inside the function', input_number)
#     return a
#
# output_number = DoubleValue(14)
# print('After the function', input_number)
#
# # You can make a variable within a function global (' global x') but its not a good method moving forward.

x = 4
print('Value and id of x before the function ', x, id(x))

def MultiplyTheValue(input):        # Try removing the global and see the id changes
    global x
    x = input * 2
    print('Value and id of x inside the function ', x, id(x))
    return x

output = MultiplyTheValue(x)
print('Value and id of X after the function ', x, id(x))

def noReturn(): # Functions can return none
    pass
print(noReturn())

# Classes and Objects

print(dir('')) # Returns all methods for a certain object - In this case the string!

print(len(dir(''))) # underscore methods are generally internal to the program
print(len([i for i in dir('') if i[:2] != '__']))

class Pizza:
    def __init__(self):
        self.toppings = []
        self.base = 'classic'
        self.sauce = 'tomato'

class Cart:
    def __init__(self):
        self.items = []
        self.code = None
        self.customer = None

    def receipt (self):
        return (f"Welcome {self.customer}\n\nYour items: \n{''.join(self.items)}\nDiscount code:{self.code}\n")

x = Cart()


x.items = ["Turntable ", "Microphone ", "Mixer "]  # Variables imbedded in the obj and we are assigning values
x.code = 'HAPPY2021'                               # to these variables
x.customer = 'Will'

print(x.receipt())

y = Cart()
y.items =['Drumsticks ', 'Guitar ', 'Laptop ']
y.code = 'GOLUCKY2021'
y.customer = 'Alice'
print(y.receipt())

class Trolley(Cart):
    def __init__(self):
        self.items = []
        self.customer = ''
        self.code = ''

    def currentbasket(self):
        print('Your basket currently includes:\n', ''.join(self.items))

z = Trolley()
z.items = ['Fish Tank ', 'Wire Cutters ', 'iPhone ']

print(z.receipt())
print(z.currentbasket())
