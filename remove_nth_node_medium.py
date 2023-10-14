####    Given the head of a linked list, remove the nth node from the end of the list and return its head.



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        current = head
        size = 0
        while(current != None):
            size += 1
            current = current.next
        index = 0
        current = head
        while(current != None and index < size - n - 1):
            index += 1
            current = current.next
        if (current == head):
            if (size == 2):
                if (n == 1):
                    head.next = head.next.next
                    return head
                elif (n == 2):
                    return head.next
            else:
                if (size == 1):
                    return None
                else:
                    if (n == size):
                        return head.next
                    elif (n == size - 1):
                        temp = current.next.next
                        current.next = temp
                        return head
        else:
            temp = current.next.next
            current.next = temp
            return head

        
