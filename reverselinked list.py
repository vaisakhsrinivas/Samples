# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head:[ListNode]) -> [ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

head = ListNode(1)
ListNode(2)
ListNode(3)
ListNode(4)
print(Solution.reverseList(self, head))