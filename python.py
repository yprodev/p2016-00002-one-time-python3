# Python v3.5.1
# --- One Line Comment ---

'''

	Multiline comment - we use three single quotes

'''

# We are importing random number generator
import random
import sys
# We are importing operating system module
import os

# To print out something use command print
print('Hello World')

# Let create a string data type variable
name = 'John'
# Print out this variable
print(name)

'''
	Five Basic Data Types in Python:
		Numbers
		Strings
		Lists
		Tuples
		Dictionaries

	There are 7 basic algorithmitic operators:
		+ - plus
		- - minus
		* - multiplication
		/ - division
		% - modulus
		** - exponensial calculation (like ^ - power of)
		// - ...

'''

# Working with algorithmitic operators
print("5 + 2 = ", 5 + 2)
print("5 - 2 = ", 5 - 2)
print("5 * 2 = ", 5 * 2)
print("5 / 2 = ", 5 / 2)
print("5 % 2 = ", 5 % 2)
print("5 ** 2 = ", 5 ** 2)
print("5 // 2 = ", 5 // 2)

# Order of operations matters!

# How to put a qoute inside String Data Type
# or How to put a qoute in qoutes
# USE \

qoute = 'Mother\'s name'
print(qoute)

# Put inside a variable a multiline string
multi_string = '''
Some text
Some more text
End of the text
'''
print(multi_string)

# We may print out this strings in a very cool way
# %s - means String Data Type
print('%s %s %s' % ('I like the quite', qoute, multi_string))

# We may print five new lines
# new line - \n
print('\n' * 5)

# We need to print this if we don't want to have a new line on the screen
print('I don\'t want a new line', end=' ')
# Here is a print that must be on the new line but he doesn't
print('A new line?')




'''
	--------------------------------------------------------
											Working with lists
	--------------------------------------------------------
'''

# Creating a simple list
grocery_list = ['Juice', 'Tomatoes', 'Potatoes',
								'Bananas']

# Print out the first item
print('First item in the list is', grocery_list[0])

# We may change the value of the first item in that list
grocery_list[0] = 'Green Juice'

# Print out modified value of the first item
print('First item in the list is', grocery_list[0])

# Print out a subset of the list
# From 1st item to third, BUT NOT INCLUDING THE THIRD
print('Range from the list', grocery_list[1:3])

# We may include list inside other lists
other_events = ['Wash Car', 'Pick Up Kids', 'Cash Check']
to_do_list = [other_events, grocery_list]

# Let's print out that list of lists
print(to_do_list)

# Lets print out second item of the second list
print(to_do_list[1][1])

# We may append items to the list
grocery_list.append('Onions')
print(to_do_list)

# We may insert item at the very specific index
grocery_list.insert(1, 'Pickle')
print(to_do_list)

# We may remove item from the list
grocery_list.remove('Pickle')
print(to_do_list)

# Try to sort items in the list
grocery_list.sort()
print(grocery_list)

# Try to sort items in the reverse order
grocery_list.reverse()
print(grocery_list)

# To delete an item we may use this:
del grocery_list[4]
print(grocery_list)

# We can combine lists like strings
to_do_list2 = other_events + grocery_list
print(to_do_list2)

# We may get last item alphabeticaly
print(max(to_do_list2))

# We may get a minimum item that comes first alphabeticaly
print(min(to_do_list2))




'''
	--------------------------------------------------------
										Working with Tuples
	--------------------------------------------------------
'''

# Tuples are surrounded by ()
# We CAN NOT change a tuple
# We can change a tuple ONLY if we convert tuple into a list
# Then do stuff we need to do with tuple (converted)
# And then convert this list beckwards in the tuple
pi_tuple = (3,1,4,1,5,9)

# Converting a tuple into a list
new_list = list(pi_tuple)

# Convertin a list into a tuple
new_tuple = tuple(new_list)

# We may discover the lenght of the tuple
len(new_tuple)

# Get the minimum from the tuple using min function
min(new_tuple)

# Get the maximum from the tuple using max function
max(new_tuple)




'''
	--------------------------------------------------------
									Working with Dictionaries
	--------------------------------------------------------
'''

# Creating a dictionary
super_villains = {'Fiddler' : 'Isaac',
									'Captain Cold' : 'Leonard Snart',
									'Weather Wizard' : 'Mark Mardon',
									'Mirror Master' : 'Sam Scudder',
									'Pied Piper' : 'Thomas Peterson'}

# Let's print out the value from the dictionary
print(super_villains['Captain Cold'])

# Let's delete somebody from the list
del super_villains['Fiddler']
print(super_villains)

# We may change key value
super_villains['Pied Piper'] = 'Hartley Rathaway'
print(super_villains['Pied Piper'])

# We can find out the lenth of our dictionary
dic_len = len(super_villains)
print(dic_len)

# We can get value from this dictionary
print(super_villains.get('Pied Piper'))

# Let's print out keys in our dictionary
print(super_villains.keys())

# The same thing we are going to do with values
print(super_villains.values())











