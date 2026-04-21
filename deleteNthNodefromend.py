class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteNthNodeFromeEnd(self, head: ListNode, n:int) -> ListNode:

        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next

    def createListNode(self, h) -> ListNode:

        head = ListNode(h[0])
        current = head
        for i in range(1, len(h)):
            current.next = ListNode(h[i])
            current = current.next
        return head

        '''dummy = ListNode()
        current = dummy

        for val in h:
            current.next = ListNode(val)
            current = current.next
        return dummy.next'''

    def printListNode(self, head: ListNode) -> ListNode:
        current = head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")


s = Solution()
head = s.createListNode([1, 2, 3, 4])
s.printListNode(head)
n = 2
s.deleteNthNodeFromeEnd(head, n)
s.printListNode(head)


