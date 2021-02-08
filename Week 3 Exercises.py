import _datetime
date = _datetime.date.today()



ExampleString = ("""Greetings! My name is William and I'm from the UK. Someday I hope to get to Japan, any suggestions? 
I want to do that because I would like to eat bluefin tuna, 
which is quite hard to find but I suppose one day I will succeed.\n\n\n
William edited the story on the 8th February 2021""")

file = open("SampleStory.txt", 'w')
file.write(ExampleString)
file.close()

file = open("SampleStory.txt", 'r')
print(file.read())




