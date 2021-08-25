from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        f = [[float("inf")] * n for _ in range(k + 2)]
        f[0][src] = 0
        for t in range(1, k + 2):
            for j, i, cost in flights:
                f[t][i] = min(f[t][i], f[t - 1][j] + cost)
        
        ans = min(f[t][dst] for t in range(1, k + 2))
        return -1 if ans == float("inf") else ans

    def findCheapestPrice2(self,n:int,flights: List[List[int]], src: int, dst: int, k: int) -> int:
        f = [float("inf")] * n
        f[src] = 0
        ans = float("inf")
        for t in range(1, k + 2):
            g = [float("inf")] * n
            for j, i, cost in flights:
                g[i] = min(g[i], f[j] + cost)
            f = g
            ans = min(ans, f[dst])
        
        return -1 if ans == float("inf") else ans

n = 3
edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0 
dst = 2
k = 1

so =Solution()

print(so.findCheapestPrice2(3,edges,src,dst,k))