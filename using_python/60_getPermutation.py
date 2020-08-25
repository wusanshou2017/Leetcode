# 给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

# "123"
# "132"
# "213"
# "231"
# "312"
# "321"

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorials, nums = [1], ['1']
        for i in range(1, n):
            # generate factorial system bases 0!, 1!, ..., (n - 1)!
            factorials.append(factorials[i - 1] * i)
            # generate nums 1, 2, ..., n
            nums.append(str(i + 1))
        
        # fit k in the interval 0 ... (n! - 1)
        k -= 1
        
        # compute factorial representation of k
        output = []
        for i in range(n - 1, -1, -1):
            idx = k // factorials[i]
            k -= idx * factorials[i]
            
            output.append(nums[idx])
            del nums[idx]
        
        return ''.join(output)



so = Solution()
print(so.getPermutation(3,2))
