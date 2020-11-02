# given two sorted linked lists, merge them into a new sorted linkedlist 

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

        
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        # set iterators
        dummy = ListNode(0)
        current = dummy

        #traverse linked list, looking for lower value of each 
        while l1 and l2: 
            if l1.val < l2.val:
               current.next = l1
               l1 = l1.next 
            else:
                current.next = l2 
                l2 = l2.next 
            current = current.next

        #traverse rest of the linkedlist
        if l1:
            current.next = l1
        else:
            current.next = l2
        return dummy.next

    def printList(self, list1: ListNode):
        # print a linked list
        dummy = list1
        res = ""
        while dummy:
            if dummy.next:
                res += str(dummy.val) + ", "
            else:
                res += str(dummy.val)
            dummy = dummy.next 
        print(res)



# sample test 

node1 = ListNode(1)
node5 = ListNode(5)
node8 = ListNode(8)
node1.next = node5
node5.next = node8

node4 = ListNode(4)
node7 = ListNode(7)
node9 = ListNode(9)
node4.next = node7
node7.next = node9

s = Solution()

list1 = node1
s.printList(list1)
list2 = node4 
s.printList(list2)
result = s.mergeTwoLists(list1, list2)
s.printList(result)

