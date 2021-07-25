# import library
import re

# url link
s = 'https://www.google.com/'

# finding the protocol
obj1 = re.findall('(\w+)://',
				s)
print(obj1)

# finding the hostname which may
# contain dash or dots
obj2 = re.findall('://www.([\w\-\.]+)',
				s)
print(obj2)
