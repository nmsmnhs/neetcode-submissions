class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = [char.lower() for char in s if char.isalnum()]
        if stripped == list(reversed(stripped)):
            return True
        return False
        