# Python code to demonstrate
# to remove all the characters
# except numbers and alphabets

import re

# initialising string
ini_string = "123abcjw:, .@! eiw"

# printing initial string
print ("initial string : ", ini_string)

# function to demonstrate removal of characters
# which are not numbers and alphabets using re

result = re.sub('[\W_]+', '', ini_string)

# printing final string
print ("final string", result)
