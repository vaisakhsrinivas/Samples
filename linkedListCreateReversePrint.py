# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def createList(self, arr):
        dummy = ListNode()
        # head = ListNode(arr[0])
        # current = head
        current = dummy
        for val in arr: # for val in arr[1:]:
            # current.next = ListNode (val)
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    def reverseList(self, head:[ListNode]) -> [ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def printList(self, head):
        current = head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

s = Solution()
head = s.createList([1, 2, 3, 4])
s.printList(head)
s.printList(s.reverseList(head))