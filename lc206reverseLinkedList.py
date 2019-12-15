from typing import List, Union

class ListNode:

    # Function to initialise the node object
    def __init__(self, data):
        self.val = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None
    # This function prints contents of linked list
    # starting from head
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.val)
            temp = temp.next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        stack = []
        while(head and head.next != None):
            stack.append(head.val)
            head = head.next
        temp = head
        while stack:
            temp.next = ListNode(stack.pop())
            temp = temp.next
        return head
    # Iterative one loop solution
    def reverseListIter(self, head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

    def reverseListRecursive(self, head):
        return self._reverse(head)

    def _reverse(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)

# Code execution starts here
if __name__=='__main__':

    # Start with the empty list
    # [2,4,3]
    # [5,6,4]
    llist1 = LinkedList()

    llist1.head = ListNode(1)
    second = ListNode(2)
    third = ListNode(3)
    four = ListNode(4)
    five = ListNode(5)
    llist1.head.next = second; # Link first node with second
    second.next = third # Link second node with the third node
    third.next = four
    four.next = five

    s = Solution()
    s.reverseList(llist1.head)