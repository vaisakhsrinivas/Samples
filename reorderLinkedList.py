class LinkedList:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def createLinkedList(arr):
    head = LinkedList(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = LinkedList(arr[i])
        current = current.next
    return head

def printLinkedList(head):
    values = []
    current = head
    while current:
        values.append(current.data)
        current = current.next
    print(values)

class Solution:

    def reorderList(self, head):
        if not head or not head.next:
            return head

        # find middle node
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        secondhalfhead = slow.next
        previous = None
        slow.next = None

        while secondhalfhead:
            nextnode = secondhalfhead.next
            secondhalfhead.next = previous
            previous = secondhalfhead
            secondhalfhead = nextnode

        # merge two halves
        firsthalf = head
        secondhalf = previous
        while secondhalf:
            tempfirst = firsthalf.next
            tempsecond = secondhalf.next

            firsthalf.next = secondhalf
            secondhalf.next = tempfirst

            firsthalf = tempfirst
            secondhalf = tempsecond



if __name__ == "__main__":
    head = [2,4,6,8,10]
    head2 = [2,4,6,8]
    #head
    createdllist = createLinkedList(head)
    printLinkedList(createdllist)
    s = Solution()
    s.reorderList(createdllist)
    printLinkedList(createdllist)
    #head2
    createdllist2 = createLinkedList(head2)
    printLinkedList(createdllist2)
    s.reorderList(createdllist2)
    printLinkedList(createdllist2)