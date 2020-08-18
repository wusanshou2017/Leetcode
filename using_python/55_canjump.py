# 输入: [2,3,1,1,4]
# 输出: true
# 解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。

class Soluiton:
    def canJump(self, nums: List[int]) -> bool:
        n , greedy = len(nums),0
        for i in range(n):
            if i <=greedy:
                greedy = max(greedy,i+nums[i])
                if greedy >=n-1:
                    return True

        return False