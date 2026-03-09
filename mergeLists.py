class Node(object):
    def __init__(self, value: None):
        self.value = value
        self.next = None


def mergeList(list1: Node, list2: Node):
    newList = Node()
    current = newList  # newList points to where current points

    while list1 and list2:
        if list1.value > list2.value:
            current.next = list2
            list2 = list2.next
        else:
            current.next = list1
            list1 = list1.next
        newList = newList.next

    if list1:
        current.next = list1
    if list2:
        current.next = list2

    return current.next
