func twoSum(nums []int, target int) []int {
    res := make([]int,0)
    for  i, num1 := range nums{
		
		num2 := target-num1
		for j:=i+1;j<len(nums);j++{
			if nums[j]==num2 {
				res =append(res,i)
				res =append(res,j)
				return res
			}
		}
	}
    return res
}