#create linkedlist

from typing import TypeAlias


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head

    def insertEnd(self, val):

        self.tail.next = Node(val)
        self.tail = self.tail.next

    def remove(self, index):
        i = 0
        current = self.head
        while i < index and current:
            i += 1
            current = current.next

        if current and current.next:
            if current.next == self.tail:
                self.tail = current
            current.next = current.next.next


    def reverse(self, head) -> Node:
        current = head
        prev = None

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        return prev

    def printlist(self):
        current = self.head.next
        while current:
            print(current.val, end = ' ')
            current = current.next
        print()



l = linkedlist()
l.insertEnd(1)
l.insertEnd(2)
l.insertEnd(3)

l.head.next = l.reverse(l.head.next)
l.printlist()
l.remove(2)
l.printlist()
