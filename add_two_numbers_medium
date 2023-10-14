####You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

#####You may assume the two numbers do not contain any leading zero, except the number 0 itself.



# Definition for singly-linked list.
#class ListNode(object):
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        returnList = ListNode()
        current = returnList
        carriedOver = 0
        firstList = l1
        secondList = l2
        while (not (firstList == None) or not(secondList == None)):
            if (firstList == None):
                firstNum = 0
            else:
                firstNum = firstList.val
            if (secondList == None):
                secondNum = 0
            else:
                secondNum = secondList.val
            current.val = (firstNum + secondNum + carriedOver) % 10
            carriedOver = int((firstNum + secondNum + carriedOver) / 10)
            firstList = None if (firstList == None) else firstList.next
            secondList = None if (secondList == None) else secondList.next
            if (not(firstList == None) or not(secondList == None)):
                current.next = ListNode()
                current = current.next
        while (carriedOver > 0):
            current.next = ListNode()
            current = current.next
            current.val = carriedOver % 10
            carriedOver = int(carriedOver / 10)


        return returnList
        
