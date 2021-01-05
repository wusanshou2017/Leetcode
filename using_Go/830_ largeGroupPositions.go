package main
import (
    "fmt"
)


func largeGroupPositions (s[] string) [][]int{
    res:=make([]int,0)
    slow_ptr :=0
    fast_ptr :=0 
    n:= len(s)
    for slow_ptr<n{
        for fast_ptr<n && s[fast_ptr]==s[slow_ptr]{
            fast_ptr++
        }
        if (fast_ptr-slow_ptr)>2{        
            res =append(res, []int{slow_ptr,fast_ptr-1})
            slow_ptr =fast_ptr
        }else{
            slow_ptr++
        }
    }
    return res
}