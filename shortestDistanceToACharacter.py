# Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.

# The distance between two indices i and j is abs(i - j), where abs is the absolute value function.

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
    # s = "loveleetcode", c = "e"
    # Output: [3,2,1,0,1,0,0,1,2,2,1,0]
        prev = -99999
        res = [None] * len(s)

        for i in range(len(s)):
            if s[i] == c:
                prev = i
            res[i] = i - prev
            

        prev = 99999
        for i in range(len(s)-1, -1, -1):
            if s[i] == c:
                prev = i
            res[i] = min(res[i], prev-i)

        return res
    
    
        
