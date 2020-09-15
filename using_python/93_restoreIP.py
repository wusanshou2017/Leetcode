from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s)<4 or len(s)>12:
            return []

        res = []

        def backtrack(track, start, s):
            # 满四段且用光所有字符串
            if len(track) == 4 and start == len(s):
                res.append('.'.join(track))
            # 满四段但没用光所有字符串
            if len(track) == 4 and start < len(s):
                return

            for l in range(1, 4):
                # 字符不存在,超出边界，最后一个字符的索引为s[start + l - 1]
                if start + l - 1 >= len(s):
                    return
                # 若选择长度超过2的字串，则不能是'0'开头
                if l >= 2 and s[start] == "0":
                    return
                tmp = s[start:start + l]
                # 长度为3的字串，取值不能大于225
                if l == 3 and int(tmp) > 255:
                    return
                backtrack(track + [tmp], start + l, s)

        backtrack([], 0, s)
        return res