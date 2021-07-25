# Python3 code to find sequences of one upper
# case letter followed by lower case letters
import re

# Function to match the string
def match(text):
		
		# regex
		pattern = '[A-Z]+[a-z]+$'
		
		# searching pattern
		if re.search(pattern, text):
				return('Yes')
		else:
				return('No')

# Driver Function
print(match("Geeks"))
print(match("geeksforGeeks"))
print(match("geeks"))
