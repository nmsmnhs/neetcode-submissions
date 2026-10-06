class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left != right and left != right + 1:
            if s[left].isalnum() == False:
                left += 1
                continue
            if s[right].isalnum() == False:
                right -= 1
                continue
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
                continue
            else:
                return False
        return True

        