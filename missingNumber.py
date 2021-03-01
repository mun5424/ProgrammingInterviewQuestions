# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = len(nums)
        # n * (n+1) / 2
        totalSum = int(count * (count + 1 ) / 2) 
        arraySum = 0
        for i in range(0, count): 
            arraySum += nums[i]
        
        return totalSum - arraySum