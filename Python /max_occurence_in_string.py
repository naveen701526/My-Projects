# Python program to return the maximum occurring character in the input string
ASCII_SIZE = 256

def getMaxOccuringChar(str):
	# Create array to keep the count of individual characters
	# Initialize the count array to zero
	count = [0] * ASCII_SIZE

	# Utility variables
	max = -1
	c = ''

	# Traversing through the string and maintaining the count of
	# each character
	for i in str:
		count[ord(i)]+=1;

	for i in str:
		if max < count[ord(i)]:
			max = count[ord(i)]
			c = i

	return c

str = "sample string"
print("Max occurring character is " + getMaxOccuringChar(str))

