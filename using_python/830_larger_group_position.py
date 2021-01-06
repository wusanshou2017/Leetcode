from typing import List
# 示例 1：

# 输入：s = "abbxxxxzzy"
# 输出：[[3,6]]
# 解释："xxxx" 是一个起始于 3 且终止于 6 的较大分组。
# 示例 2：

# 输入：s = "abc"
# 输出：[]
# 解释："a","b" 和 "c" 均不是符合要求的较大分组。
# 示例 3：

# 输入：s = "abcdddeeeeaabbbcd"
# 输出：[[3,5],[6,9],[12,14]]
# 解释：较大分组为 "ddd", "eeee" 和 "bbb"


def FindPosition(s: str) -> [[int]]:
    n = len(s)
    res = []
    slow_ptr, fast_ptr = 0, 0
    while slow_ptr < n - 1:
        fast_ptr = slow_ptr + 1
        while fast_ptr < n and s[fast_ptr] == s[slow_ptr]:
            fast_ptr += 1

        if fast_ptr - slow_ptr > 2:
            res.append([slow_ptr, fast_ptr - 1])
            slow_ptr = fast_ptr
        else:
            slow_ptr += 1

    return res


print(FindPosition("aa"))
