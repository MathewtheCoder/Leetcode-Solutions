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
    def hasCycleNaive(self, head: ListNode) -> bool:
        prevValues = []
        temp = head
        while(temp != None):
            if(temp in prevValues):
                return True
            prevValues.append(temp)
            temp = temp.next
        return False

    # 3 -> 1 -> 2
    #      |____|
    def hasCycle(self, head: ListNode) -> bool:
        temp = ""
        while (head != None):
            if (head.next == None):
                return False
            if (head.next == temp):
                return True
            nex = head.next
            head.next = temp
            head = nex

        return False
    # 3 -> 1 -> 2 -> 1
    def hasCycle(self, head: ListNode) -> bool:
        slow_p = head
        fast_p = head
        while(slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                print "Found Loop"
                return True
        return False




