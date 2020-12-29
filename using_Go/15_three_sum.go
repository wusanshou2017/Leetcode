package main
 
import (
    "fmt"
    "sort"
)
 
//  to do get the target=0 which sum is   
func xsum(nums []int){
     sort.Ints(nums)
     res:= make([]int,8)
     if len(nums)<3 || nums[0]>0 || nums[len(nums)-1]<0{
        empty := make([]int,0,0)
        return empty
     }
     n := len(nums)
     dicSum:=make(map[[]int]int ,8)
     for i:=0;i<n;i++{
         for j:= i+1;j<n;j++{
            temp_key := make{i,j}
            dicSum[temp_key]= nums[i] + nums[j]            
         }
     }
     for idx,num:= range(nums){
        for k,v:=range(dicSum){
            if v ==-num{
                temp_index:= make{}
                temp_flag:=true
                for _,val:=range(k) {
                    if val==idx{
                        temp_flag=false                
                    }
                    temp_index=append(temp_index, val)
                }
                if temp_flag{
                    temp_index=append( temp_index,idx)
                    sort.Ints(temp_index)
                    res=append(res,temp_index)
                }

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
