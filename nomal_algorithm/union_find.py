class UnionFind():
    """并查集类"""

    def __init__(self, n):
        """长度为n的并查集"""
        # 建图
        self.uf = [i for i in range(n + 1)]
        # 所有变量独立
        self.sets_count = n

    def find(self, p):
        """查找p的根结点(祖先)"""
        # while self.uf[p]>=0:
        # p = self.uf[p]
        # return p
        # 极端条件下 退化为链表

        """尾递归"""
        if self.uf[p] < 0:
            return p
        self.uf[p] = self.find(self.uf[p])
        return self.uf[p]

    def union(self, p, q):
        """连通p,q 让q指向p"""
            """连通p,q 让q指向p"""
        proot = self.find(p)
        qroot = self.find(q)
        if proot == qroot:
            return
        elif self.uf[proot] > self.uf[qroot]:   # 负数比较, 左边规模更小
            self.uf[qroot] += self.uf[proot]
            self.uf[proot] = qroot
        else:
            self.uf[proot] += self.uf[qroot]    # 规模相加
            self.uf[qroot] = proot
        self.sets_count -= 1                    # 连通后集合总数减一

    def is_connected(self, p, q):
        """判断节点p和q是否已经连通"""
            return self.find(p) == self.find(q)
