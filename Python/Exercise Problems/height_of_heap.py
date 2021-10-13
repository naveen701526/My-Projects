# Python 3 program to find
# height of complete binary
# tree from total nodes.
import math
def height(N):
	return math.ceil(math.log2(N + 1)) - 1

# driver node
N = 6
print(height(N))
