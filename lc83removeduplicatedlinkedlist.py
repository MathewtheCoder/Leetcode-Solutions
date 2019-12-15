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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        temp = head
        unique = head
        while(temp != None):
            if(temp.val != unique.val):
                unique.next = temp
                unique = temp
            temp = temp.next
        # In case of [] or non unique last node [1,1]
        if(unique != None):
            unique.next = None
        return head
    # Recursive solution
    def deleteDuplicatesRecursive(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        if head.val == head.next.val:
            head = self.deleteDuplicatesRecursive(head.next)
            return head
        else:
            head.next = self.deleteDuplicatesRecursive(head.next)
            return head

        return head



# Code execution starts here
if __name__=='__main__':
    llist1 = LinkedList()

    llist1.head = ListNode(1)
    second = ListNode(1)
    third = ListNode(2)
    fourth = ListNode(2)
    llist1.head.next = second; # Link first node with second
    second.next = third; # Link second node with the third node
    third.next = fourth
    # llist1.printList()
    sol = Solution()
    uniqueLlist = LinkedList()
    uniqueLlist.head = sol.deleteDuplicates(llist1.head)
    uniqueLlist.printList()