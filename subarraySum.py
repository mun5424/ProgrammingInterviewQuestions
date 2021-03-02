#Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(0, len(nums)):
            curr = 0
            j = i + 1
            while curr <= k:
                curr += nums[j]
                j += 1
                if (curr == k):
                    count += 1
        return count     