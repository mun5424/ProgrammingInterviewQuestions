class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1) 
        n = len(text2)
        
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)] 
            
        for i in range(1, m+1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]: 
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]) 
                    
        for i in range(len(dp)):
            print(dp[i])

        return dp[m][n]

            
# ABCD text1
# AB   text22


 #     A B C D E
 #   0 0 0 0 0 0
 # C 0 0 0 1 1 1       
 # D 0 0 0 1 2 2
 # A 0 1 1 1 2 2 
 # B 0 1 2 2 2 2 

# ('abcde', 'cdab')

8888888888883338383383838883777733722216161234599876