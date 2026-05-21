class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.front = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.front = self.head
        self.presence = {}

    def get(self, key: int) -> int:
        if key in self.presence:
            node = self.presence[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.presence:
            node = self.presence[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            node.value = value
        else: 
            if len(self.presence) >= self.capacity:
                self.removeFromTail()
            node = Node(key,value)
            self.presence[key] = node
            self.insertIntoHead(node)

    def removeFromList(self, node):
        node.front.next = node.next
        node.next.front = node.front
    
    def insertIntoHead(self, node):
        headNext = self.head.next
        self.head.next = node 
        node.front = self.head 
        node.next = headNext 
        headNext.front = node
    
    def removeFromTail(self):
        if len(self.presence) == 0:
            return
        tail_node = self.tail.front
        del self.presence[tail_node.key]
        self.removeFromList(tail_node)


def main():
    lRUCache = LRUCache(2);
    lRUCache.put(1, 1)        # cache is {1=1}
    lRUCache.put(2, 2)        # cache is {1=1, 2=2}
    print(lRUCache.get(1))    # return 1
    lRUCache.put(3, 3)        # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    print(lRUCache.get(2))    # returns -1 (not found)
    lRUCache.put(4, 4)        # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    print(lRUCache.get(1))    # return -1 (not found)
    print(lRUCache.get(3))    # return 3
    print(lRUCache.get(4))    # return 4

main()