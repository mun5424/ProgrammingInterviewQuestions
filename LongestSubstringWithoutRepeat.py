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

    # questions - what to do when you want the actual substring? and not the length 
    def LongestSubstring(self, s: str) -> int:
        map = {}
        res = 0
        start = 0
        startIndexOfMax = 0
        maxLength = 0
        for i in range (1,len(s)):
            currentChar = s[i]
            if currentChar not in map: 
                # characters not in the map, add it to the map 
                map[currentChar] = i
            else:
                # character in the map. check if the occurrence is before or after the crurrent starting index
                if map[currentChar] >= start:
                    # the iterating index - the starting index of the current character
                    currentLength = i - start
                    if maxLength < currentLength:
                        maxLength = currentLength
                        #update start index of maximum character because we just found that the maximum index starts on this character
                        startIndexOfMax = start
                    start = pos[currentChar] + 1 
                pos[currentChar] = i

        # needs to do another run in case it misses the last one
        currentLength = i - start
        if maxLength < currentLength:
            maxLength = currentLength
            startIndexOfMax = start
        
        return s[startIndexOfMax : startIndexOfMax + maxLength]  
