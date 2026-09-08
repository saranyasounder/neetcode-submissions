class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []

        for char in s:
            if char in pairs:
                # closing bracket: check if it matches the top of the stack
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:
                # opening bracket: push it
                stack.append(char)

        return not stack