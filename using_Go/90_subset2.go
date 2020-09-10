package partition

import (
    "fmt"
)


func subsetsWithDup(nums []int) [][]int {
    n :=len(nums)
    sort.Ints(nums)
    var path []int
    var res [][]int

    dfs(0,n,nums,path,&res)
    return res 
}

func dfs (start int, end int, nums []int, path []int, res *[][]int ) {
        
        for i:=start;i<end;i+=1{
            if (i>start && nums[i]==nums[i-1]){
                continue
            }
            path := append(path, nums[i])
            res := append(*res,path)
            dfs(i+1,end,nums,path,res)
        }
}


func demo(nums []int) []int{

    sorted(nums)

    return nums

}

func sorted(nums [] int){

    

}