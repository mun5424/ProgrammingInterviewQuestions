class Solution:
    def longestPalindrome(self, s: str) -> str:
        j = 0 
        start = 0
        end = 0
        for i in range(0, len(s)):
            odds = expandFromCenter(s, i, i)
            evens = expandFromCenter(s, i, i + 1)
            maxCurrent = max(odds, evens)
            if maxCurrent > end - start:
                start = i - (maxCurrent - 1) / 2
                end = i - (maxCurrent) / 2

        return s[start:end+1]

    def expandFromCenter(self, s, begin, end):
        left = begin
        right = end
        while (left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1
        return right - left - 1
           


            