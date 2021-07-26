package main
import (
    "fmt"
)
func max_int(a int ,b int ) int{
    if (a>b){
        return  a 
    }else{
        return  b
    }

}

func longestOnes(A []int, K int) int {
    res:=0
    slow :=0
    fast :=0 
    n := len(A)
    for slow<n && fast<n {
        if (A[fast]>0 || K>0){
            if A[fast]==0{
                K--
            }
            fast++
        }else{
            if (A[slow]==0){
                fast++
            }
            slow++
        }
        res = max_int(res,fast-slow)
    }
    return res
}

func main() {
    
    test_data :=[] int{1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0}
    fmt.Println(longestOnes(test_data, 2))
}
