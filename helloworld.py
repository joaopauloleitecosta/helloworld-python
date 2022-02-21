import random

""" 
this is a tutorial about the 
python language	
"""
print("Hello, World!")

# variables are created the moment you first assign a value to it
x = 10 		# type int
y = "john" 	# type str
print(x)

#casting and get the type
x = str(3)
print(type(x))

# string variables can be single or double quotes
name = "Joao"
name = 'Joao'

#case-sensitive
a = 4 
A = "Sally"

# many values to multiple variables
x, y, z = "orange", "banana", "apple"
print(x)
print(y)
print(z)

# one value to multiple variables
x = y = z = 100
print(x)
print(y)
print(z)

# unpack a collection
fruits = ["melon", "lemon", "strawberry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# output variables
x = "awesome"
print("Python is " + x)

# global variables can by used inside or outside of functions
x = "I am a global."

def myfunc():
	print(x)

myfunc()

""" built-in Data Types
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
getting the Data Type: type()
"""

# using random number
print("random number: " + str(random.randrange(1, 10)))

# indentation is important
if 5 > 2:
	print("5 > 2")

