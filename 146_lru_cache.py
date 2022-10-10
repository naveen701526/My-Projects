class Node:
    # key, val, next, prev
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None

""" Time Complexity:  O(1), Space Complexity: O(capacity) """
class LRUCache:
    # create hasmap and it's capacity, doubly with lru == head, mru == tail
    def __init__(self, capacity: int):
        self.cacheMap = {}
        self.capacity = capacity
        self.lru = Node(0, 0)
        self.mru = Node(0, 0)
        self.lru.next = self.mru
        self.mru.prev = self.lru

    # removes the node
    def remove(self, node):
        nextNode , prevNode = node.next , node.prev
        nextNode.prev, prevNode.next = prevNode, nextNode

    # insert at MRU
    def insert(self, node):
        prev = self.mru.prev
        self.mru.prev = node
        node.next = self.mru
        node.prev = prev
        prev.next = node

    # return the cache's val withh the key | Updates the order of cache -> removes the node and link it to MRU
    def get(self, key: int) -> int:
        if key in self.cacheMap:
            self.remove(self.cacheMap[key])
            self.insert(self.cacheMap[key])
            return self.cacheMap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cacheMap:
            self.remove(self.cacheMap[key])
    
        self.cacheMap[key] = Node(key, value)
        self.insert(self.cacheMap[key])

        if len(self.cacheMap) > self.capacity:
            lruNode = self.lru.next
            self.remove(lruNode)
            del self.cacheMap[lruNode.key]