package main
 
import (
    "fmt"
    "sort"
)
 
//  to do get the target=0 which sum is   
func threeSum(nums []int)[][]int{
     n:=len(nums)
     sort.Ints(nums)
     res:= make([][]int,0)
     for first:= 0;first<n;first++{
        if first>0 && nums[first] ==nums[first-1]{
            continue
        }
        third :=n-1
        target:=  0- nums[first]
        for second:= first+1;second<n;second++{
            if second>first+1 && nums[second]==nums[second-1]{
                continue
            }
            for second<third &&nums[second]+nums[third]>target{
                third--
            }
            if second ==third{
                break
            }
            if nums[second]+nums[third] == target{
                ans = append(ans,[]int {nums[first],nums[second],nums[third]})
            }
        }
     }        
     return res
}



//  unit_test
//  
func main() {    

    fmt.Println(".")
}
