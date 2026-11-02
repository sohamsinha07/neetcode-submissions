class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currCharacters = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in currCharacters:
                currCharacters.remove(s[l])
                l += 1
            currCharacters.add(s[r])
            res = max(res, r+1 - l )
        return res
