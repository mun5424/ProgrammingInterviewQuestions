# given a list of integers and a number k, find if there is at least one subset that sums up to k

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # use dp, rows = numbers, cols = sum 
        N = len(nums)
        dp = [[False] * (k+1) for _ in range(N+1)]

        for i in range(N+1):
            dp[i][0] = True
        
        for i in range(1, k+1):
            dp[0][i] = False
        
        for i in range(1, N+1):
            for j in range(1, k+1):
                print('evaluating row ', i, ' column ', j)
                if j < nums[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]

        return dp[N][k]
    


solution = Solution()
set1 = [3, 34, 4, 12, 5, 2]
k = 9 
print(solution.subarraySum(set1, k))


