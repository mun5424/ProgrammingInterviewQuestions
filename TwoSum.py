from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    dict = {}
    for i in nums: 
        if not target-nums[i] in dict: 
            dict[nums[i]] = i
        else:
            return  [i, dict[target-nums[i]]]
    return [-1,-1]


print( twoSum([1,2,3,4,5] , 9))