class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = ''
        maxlen = 0
        for i in range(len(s)):
            if s[i] not in r:
                r += s[i]
                maxlen = len(r) if len(r) > maxlen else maxlen
            else:
                index = r.index(s[i])
                r = r[index+1:]
                r += s[i]
                maxlen = len(r) if len(r) > maxlen else maxlen
        return maxlen
