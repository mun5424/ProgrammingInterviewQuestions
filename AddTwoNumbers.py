# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution::
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        carry = 0
        current = dummy
        while (l1 and l2):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = (x + y + carry)
            carry = int(sum / 10)
            val = sum % 10
            current.next = ListNode(val) 
            current = current.next 
            if l1: 
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry > 0:
            current.next = ListNode(carry)
            
        return dummy.next