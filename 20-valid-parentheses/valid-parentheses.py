class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char in mapping:
                # Closing bracket
                top = stack.pop() if stack else '#'
                if mapping[char] != top:
                    return False
            else:
                # Opening bracket
                stack.append(char)

        return not stack
