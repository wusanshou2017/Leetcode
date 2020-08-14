class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == "[" or char == "{":
                stack.append(char)

            if char == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False

            if char == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    return False

            if char == "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    return False

        if not stack:
            return False
        return True


so = Solution()
print(so.isValid("()"))
