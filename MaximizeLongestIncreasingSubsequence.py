# given two sorted linked lists, merge them into a new sorted linkedlist 
# Maximize length of increasing subsequence
# possible by replacing array element by nearest
# primes. Given an array arr[], the task is to maximize
# the length of increasing subsequence by replacing
# elements to greater or smaller prime number to
# the element


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

        
class Solution:
    def maximizeLengthOfIncreasingSubsequence(self, arr) -> int:
        maxLength = 0
        for x in range(0, len(arr)): 
            maxLength = max(maxLength, 0)



# sample test 

