
# A single node of a singly Linked List
class Node:
    # constructor
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# A Linked List class with a single head node


class LinkedList:
    def __init__(self):
        self.head = None

    # insertion method for the linked list
    def insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    # print method for the linked list
    def printLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next


def reverseList(list):
    # initialize variables
    previous = None         # `previous` initially points to None
    current = list.head     # `current` points at the first element
    following = current.next    # `following` points at the second element

    # go till the last element of the list
    while current:
        current.next = previous  # reverse the link
        previous = current      # move `previous` one step ahead
        current = following         # move `current` one step ahead
        if following:               # if this was not the last element
            following = following.next    # move `following` one step ahead

    list.head = previous


LL = LinkedList()
LL.insert(1)
LL.insert(2)
LL.insert(3)
LL.insert(4)
print("Linked List")
LL.printLL()
print("Reversed Linked List")
reverseList(LL)
LL.printLL()
