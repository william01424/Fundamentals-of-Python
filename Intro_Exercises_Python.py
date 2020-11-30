# Exercises from http://www.introtopython.org/var_string_num.html#Challenges-numbers

# Hello World - variable
# Store your own version of the message "Hello World" in a variable, and print it.

x = 'Hello World'
print(x)

# One Variable, Two Messages:
# Store a message in a variable, and then print that message.
# Store a new message in the same variable, and then print that new message

y = 'Hello my name is William and I am learning Python'
print(y)
y = 'A Great White Shark is my favourite animal in the whole world!'
print(y)

# Someone Said
# Find a quote that you like. Store the quote in a variable, with an appropriate introduction such as
# "Ken Thompson once said, 'One of my most productive days was throwing away 1000 lines of code'". Print the quote.

quote = "'Opportunities are like sunrises. If you wait too long, you will miss them'"

print("William Arthur Ward once said,", quote)

# Store your first name, in lowercase, in a variable.
# Using that one variable, print your name in lowercase, Titlecase, and UPPERCASE

name = 'william templeton'
print(name.title())
print(name.upper())
print(name.lower())

# Store your first name and last name in separate variables, and then combine them to print out your full name.

x = 'William'
y = 'Templeton'

print(x,'Ross', y)

# Choose a person you look up to. Store their first and last names in separate variables.
# Use concatenation to make a sentence about this person, and store that sentence in a variable.-
# Print the sentence.

x = 'Elon'
y = 'Musk'
print(x + ' ' + y)

new_str = (x + ' ' + y + ' ' + 'is' + ' ' + 'cool')
print(new_str)

# Stripping whitespace examples

first_name = '                  William           '
print(first_name)
print(first_name.lstrip())
print(first_name.rstrip())
print(first_name.strip())
