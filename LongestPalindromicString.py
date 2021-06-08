class Solution:
    def expandFromCenter(self, s, begin, end) -> int:
        left = begin
        right = end
        while (left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1
        return right - left - 1
           


            
    def longestPalindrome(self, s: str) -> str:
        j = 0 
        start = 0
        end = 0
        for i in range(0, len(s)):
            odds = self.expandFromCenter(s, i, i)
            # aba
            # abba
            evens = self.expandFromCenter(s, i, i + 1)
            maxCurrent = max(odds, evens)
            if maxCurrent > end - start:
                start = i - (maxCurrent - 1) / 2
                end = i - (maxCurrent) / 2

        return s[start:end+1]
 