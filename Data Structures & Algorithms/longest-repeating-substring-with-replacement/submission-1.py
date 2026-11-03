from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = defaultdict(int)

        l = 0
        highest = 0
        for r in range(len(s)):
            count[s[r]] += 1
            highest = max(highest, count[s[r]])

            if (r - l + 1) - highest > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, (r - l + 1))

        return res

