class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        res = 0
        i = 0
        j = 0
        while (i < len(s) and j < len(s)):
            if s[j] in map:
                i = max(map[s[j]], i)
            res = max(res, j - i + 1)
            map[s[j]] = j + 1
            j += 1
        return res
    # need to review this again