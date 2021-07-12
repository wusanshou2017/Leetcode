def merge_sort(nums=list):
    #取mid以及左右两个数组
    mid = len(nums)//2
    left_nums,right_nums = nums[:mid],nums[mid:]

    #递归分治
    if len(left_nums) > 1:
        left_nums = merge_sort(left_nums)
    if len(right_nums) > 1:
        right_nums = merge_sort(right_nums)

    #合并
    res = []
    while left_nums and right_nums:  #两个都不为空的时候
        if left_nums[-1] >= right_nums[-1]:  #尾部较大者
            res.append(left_nums.pop())
        else:
            res.append(right_nums.pop())
    
    res.reverse() #倒序
    return (left_nums or right_nums) + res #前面加上剩下的非空nums

lis = [7, 5, 0, 6, 3, 4, 1, 9, 8, 2]
print(merge_sort(lis)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def quick_sort(nums:[int])->[int]:
    if len(nums)<2:
        return nums

    base =nums[-1]
    pre =[ x for x in nums[:-1] if x <base]
    post = [ x for x in nums[:-1] if x >=base]
    return quick_sort(pre)+[base]+quick_sort(post)

print (quick_sort(lis))

class Solution():
    def search(nums:[int],target)->[int]:
        # start_index,last_index =0,len(nums)-1
        # while start_indexM<=last_index:
        #     if nums[start_index]!= w
        pass 


s ="武汉武汉武汉市"
print(set(s))