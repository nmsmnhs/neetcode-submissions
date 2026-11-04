from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""

        l = 0
        r = 0
        freqt = [0] * 58
        
        for i in range (len(t)):
            freqt[ord(t[i]) - ord("A")] += 1

        count = len(t)
        minlen = len(s) + 1
        start = 0

        while r < len(s):
            if freqt[ord(s[r]) - ord("A")] > 0:
                count -= 1
            freqt[ord(s[r]) - ord("A")] -= 1
            r += 1

            while count == 0:
                if r - l < minlen:
                    start = l
                    minlen = r - l
                
                if freqt[ord(s[l]) - ord("A")] == 0:
                    count += 1
                freqt[ord(s[l]) - ord("A")] += 1
                l += 1
        
        if minlen == len(s) + 1:
            return ""
        return s[start : start + minlen]

