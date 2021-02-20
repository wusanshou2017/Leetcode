package main

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
            if A[fast]>0{
                K--
            }else{
                fast++
            }
        }else{
            if (A[slow]==0){
                fast++
            }else{
                slow++
            }
        }
        res = max_int(res,fast-slow)
    }
    return res
}

func main() {
    
}
