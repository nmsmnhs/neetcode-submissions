class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        l = 0
        r = 1

        chars = set()
        chars.add(s[l])
        longest = 0

        while r < len(s):
            if s[r] in chars:
                chars.remove(s[l])
                l += 1
            else:
                chars.add(s[r])
                longest = max(longest, (r - l + 1))
                r += 1

        return longest

