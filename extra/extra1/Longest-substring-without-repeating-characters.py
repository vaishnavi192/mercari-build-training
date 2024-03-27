class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start = 0
        end = 0
        maxLength = 0
        charSet = set()
        
        while end < len(s):
            if s[end] not in charSet:
                charSet.add(s[end])
                maxLength = max(maxLength, end - start + 1)
                end += 1
            else:
                charSet.remove(s[start])
                start += 1
                
        return maxLength