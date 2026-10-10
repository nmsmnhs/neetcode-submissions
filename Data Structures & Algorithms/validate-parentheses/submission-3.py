class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            else:
                if stack == []:
                    return False
                if (char == ')' and stack[-1] == '(') or (char == ']' and stack[-1] == '[') or (char == '}' and stack[-1] == '{'):
                    stack.pop(-1)
                else:
                    return False
        if stack == []:
            return True
        else:
            return False
        