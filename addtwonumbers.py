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
    def calcSumAndCarryover(self, l1: ListNode, l2: ListNode, carryOver:int) -> List[int]:
        if(l1 != None and l2 != None):
            total = l1.val + l2.val + carryOver
        elif(l1 != None and l2 == None):
            total = l1.val + carryOver
        elif(l1 == None and l2 != None):
            total = l2.val + carryOver
        if(total > 9):
            total = total - 10
            carryOver = 1
        else:
            carryOver = 0
        return [total, carryOver]
    def addToSumLL(self, answer: Union[None, ListNode], sumTemp: Union[None, ListNode], sum1: int) -> List[ListNode]:
        if(isinstance(answer, ListNode)):
            sumTemp.next = ListNode(sum1)
            sumTemp = sumTemp.next
        else:
            answer = ListNode(sum1)
            sumTemp = answer
        return [answer, sumTemp]
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp1 = l1
        temp2 = l2
        answer = None
        sumTemp = None
        carryOver = 0
        while(temp1 != None and temp2 != None):
            [sum1, carryOver] = self.calcSumAndCarryover(temp1, temp2, carryOver)
            [answer, sumTemp] = self.addToSumLL(answer, sumTemp, sum1)
            temp1 = temp1.next
            temp2 = temp2.next
        # If first ll is more than second
        while(temp1 != None):
            [sum1, carryOver] = self.calcSumAndCarryover(temp1, temp2, carryOver)
            [answer, sumTemp] = self.addToSumLL(answer, sumTemp, sum1)
            temp1 = temp1.next
        # If first ll is more than second
        while(temp2 != None):
            [sum1, carryOver] = self.calcSumAndCarryover(temp1, temp2, carryOver)
            [answer, sumTemp] = self.addToSumLL(answer, sumTemp, sum1)
            temp2 = temp2.next
        # In case of any extra carryOver
        if(carryOver == 1):
            [answer, sumTemp] = self.addToSumLL(answer, sumTemp, carryOver)
        return answer
# Code execution starts here
if __name__=='__main__':

    # Start with the empty list
    # [2,4,3]
    # [5,6,4]
    llist1 = LinkedList()

    llist1.head = ListNode(1)
    second = ListNode(8)
    third = ListNode(3)
    llist1.head.next = second; # Link first node with second
    second.next = third; # Link second node with the third node

    llist2 = LinkedList()

    llist2.head = ListNode(0)
    second2 = ListNode(6)
    third2 = ListNode(4)

    llist2.head.next = second2 # Link first node with second
    second2.next = third2 # Link second node with the third node
    print('List 1')
    llist1.printList()
    print('List 2')
    llist2.printList()

    solution = Solution()
    sumRes = solution.addTwoNumbers(llist1.head, llist2.head)
    sumllist = LinkedList()
    sumllist.head = sumRes
    print('Sum List')
    sumllist.printList()