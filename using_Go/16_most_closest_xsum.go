package main

import (
    "fmt"
    "sort"
)
func absInt(num int) int{
    if num>=0{
        return num
    }else {
        return -num
    }
}
var MAX_INT int = 65535
func findClosestNum(nums []int,target int ) int{
//   to do
    var res int
    sort.Ints(nums)
    n := len(nums)
    if n<3{
        return -1
    }
    diff:=MAX_INT
    for i:=0;i<n-2;i++{
        l := i+1
        r := n-1
        for l<r{
            sum := nums[i]+nums[l]+nums[r]
            if (absInt(sum-target)<diff){
                diff = absInt(sum-target)
                res = sum
            }
            if (sum>target){
                r--
            }else if(sum<target) {
                l++
            }else{
                return sum
            }

        }
    }
    return res
}

// just unit test
func main(){

    test_data:=[]int {0,2,1,-3}
    fmt.Println(findClosestNum(test_data,1))
    fmt.Println("just unit test")

}
