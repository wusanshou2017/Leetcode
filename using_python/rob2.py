class Rob2():
    def rob(self,nums:[int])->int:
        dp = [0]* len(nums)
        if len(nums)<2:
            return nums[0]

        if not nums:
            return 0
        # to_do  splite the nums to two copies 
        copies1 = nums[:-1]
        copies2 = nums[1:]

        dp[0] = copies1[0]
        dp[1] = copies1[1]

        # loop in two to compare the best res
        
        res1 ,res2 =0,0

        for i in range(2,len(copies1)):
            dp[i] = max(dp[i-1],dp[i-2]+copies1[i])

        res1 =dp[len(copies1)-1]

        dp[0] = copies2[0]
        dp[1] = copies2[1]

        for i in range(2,len(copies2)):
            dp[i] = max(dp[i-1],dp[i-2]+copies2[i])

        res2 = dp[len(copies2)-1]

        return max(res1,res2)


