# Python3 program to implement stack using a
# single queue

q = []

# append operation
def append(val):

	# get previous size of queue
	size = len(q)

	# Add current element
	q.append(val)

	# Pop (or Dequeue) all previous
	# elements and put them after current
	# element
	for i in range(size):

		# this will add front element into
		# rear of queue
		x = q.pop(0)
		q.append(x)
			
# Removes the top element
def pop():

	if (len(q) == 0):

		print("No elements")
		return -1
	
	x = q.pop(0);
	return x

# Returns top of stack
def top():

	if(len(q) == 0):
		return -1
	return q[-1]

# Returns true if Stack is empty else false
def isEmpty():

	return len(q)==0

# Driver program to test above methods
if __name__=='__main__':

	s = []

	s.append(10)
	s.append(20)
	print("Top element :" + str(s[-1]))
	s.pop()
	s.append(30)
	s.pop()
	print("Top element :" + str(s[-1]))
