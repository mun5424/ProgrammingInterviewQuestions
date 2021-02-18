# Reverse a linked list
# 1 -> 2 -> 3 -> None 
# 3 -> 2 -> 1 -> None

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverseLinkedList(head):
    curr = head
    prev = None

    while True:
        print('curr value is ', curr.value)
        nextNode = curr.next
        curr.next = prev
        prev = curr
        if not nextNode:
            break
        curr = nextNode

    return curr

def printList(head):
    curr = head 
    while (curr != None):
        print(" ", curr.value)
        curr = curr.next

node1 = Node(1)
node2 = Node(2) 
node3 = Node(3)

node1.next = node2
node2.next = node3 

printList(node3)
reverseLinkedList(node1)
printList(node3)