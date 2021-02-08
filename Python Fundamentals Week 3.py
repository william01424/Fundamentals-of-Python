## The File System with Python

import os
print()
print(os.getcwd())      # Not sure why this is not printing anything?
print("The separator on this computer is: ", os.sep)

# How to navigate the file system through PowerShell (Windows)

# Commands run in windows powershell include basic ls ,cd, creating files and removed them (similar with directories)
# In order to save multiple lines for space I will not include this here - please see lecture notes for details


# Windows and Mac is available in the video - see black background for windows PWSh and light for MacOS. I wont be looking at mac OS as windows is my preffered OS


# Writing and reading files with Python


# Creating files by creating a file 'opener'

# open() 'w' = write 'r' = read 'a' = append -- there are others!!

ExampleStr = "William is a cool dude and he loves pancakes with lemon and sugar\n"

# Writing:
fileout = open("example.txt", 'w')
fileout.write(ExampleStr)
fileout.close()

# Reading:
filein = open("example.txt", 'r')
print(filein.read())
filein.close()

# Appending:

AppendingStr = "Don't forget that he also likes sharks"
fileout = open("example.txt", 'a')
fileout.write(AppendingStr)
fileout.flush() # way to pause where you are and write it to disc (saving)
fileout.close()

filein = open("example.txt", 'r')
print(filein.read()) # if file is too large you might not want to print the whole thing at once - see below

filein = open("example.txt") # filein acts as a variable
for i in filein:
    print(i)


filein = open("example.txt") # removes last character (\n is also removed?)
for i in filein:
    print(i[:-1])

    # -------------------BREAK---------------------- #

NewFileText = "My dog eats jam.\n\nMy cat drinks milk.\n\nMy fish eats fish food.\n\n"

file = open("example2.txt", 'w')
file.write(NewFileText)
file.close()

file = open("example2.txt", 'r')
print(file.read())

file = open("example2.txt", 'r')
for i in file:
    print(i.rstrip()) # this prints each line with an additional \n hence 3 spaces
    # .rstrip() removes white space that isn't within the original string
print(file.closed) # TRUE or FALSE

# We got closed = FALSE, as we didn't do <filename>.close()
# Is there another way to do this? with statements with auto close files when you exit a block of code

with open("example2.txt", 'r') as file:
    for line in file:
        print(line)

print(file.closed)

    # -------------------BREAK---------------------- #

import os

filetext = '''print("Hello, yet another world. \\nLet's count to ten!\\n")
for i in range(10):
    print(i)'''

fileout = open("Test.py", 'w')
fileout.write(filetext)
fileout.close()

