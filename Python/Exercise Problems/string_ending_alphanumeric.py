# Python program to accept string ending
# with only alphanumeric character.
# import re module

# re module provides support
# for regular expressions
import re

# Make a regular expression to accept string
# ending with alphanumeric character
regex = '[a-zA-z0-9]$'
	
# Define a function for accepting string
# ending with alphanumeric character
def check(string):

	# pass the regular expression
	# and the string in search() method
	if(re.search(regex, string)):
		print("Accept")
		
	else:
		print("Discard")
	

# Driver Code
if __name__ == '__main__' :
	
	# Enter the string
	string = "ankirai@"
	
	# calling run function
	check(string)

	string = "ankitrai326"
	check(string)

	string = "ankit."
	check(string)

	string = "geeksforgeeks"
	check(string)
