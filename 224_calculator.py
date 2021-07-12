# 示例 1：

# 输入：s = "1 + 1"
# 输出：2
# 示例 2：

# 输入：s = " 2-1 + 2 "
# 输出：3
# 示例 3：

# 输入：s = "(1+(4+5+2)-3)+(6+8)"
# 输出：23

class Solution:
    def calculate(self, s: str) -> int:
        pre, ans, stack = 0, 0, []
        sigh = 1
        # 压栈
        for c in s:
            if c == "(":
                statement0
            elif c == ")":
                stack.pop()
                statement1

            elif c.isdigital():
                stack.append(c)

            else:
                continue
