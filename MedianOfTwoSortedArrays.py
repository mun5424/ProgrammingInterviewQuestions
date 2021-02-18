# find the median of two sorted arrays
# [1, 5, 9]
# [2, 7] 
# => median of sorted arrays are 5, since if we put them all together it becomes
# [1, 2, 5, 7, 9]


from os import system


class Solution: 
    def medianOfTwoSortedArrays(self, x, y):
        if (len(x) > len(y)):
            self.medianOfTwoSortedArrays(y,x)

        # index
        low = 0
        high = len(x)
        mid = (len(x) + len(y) + 1)/ 2 # +1 to handle both odd/even 
        while (low <= high):    
            partitionX = (low + high) / 2
            partitionY = mid - partitionX

            maxLeftX = (partitionX == 0) if system.minint else x[partitionX-1] 



        return median; 