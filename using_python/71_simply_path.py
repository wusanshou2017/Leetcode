class Solution:
    def simplifyPath(self, path: str) -> str:
        seg_lst = path.split("/")
        res_lst = []
        for item in seg_lst:
            if item == "":
                continue
            if item == ".":
                continue
            if item == "..":
                if res_lst:
                    res_lst.pop()
            else:
                res_lst.append(item)
        return "/" + "/".join(res_lst)


so = Solution()

print(so.simplifyPath("/a//b////c/d//././/.."))
