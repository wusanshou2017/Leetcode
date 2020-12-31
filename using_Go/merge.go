package main

import (
    "fmt"
)

func normalize(target []int)[]int {
  
    //  对 区间进行再划分 
    //  
    //  

    mid :=  len(target)/2
    leftPart := target[:mid]
    rightPart := target[mid:]  


    part1 := normalize(leftPart)
    part2 := normalize(rightPart)

    return  merge(part1, part2)
}


func merge(leftPart []int,rightPart []int) []int{
    res := make([]int, 8)
    i:=0
    j:=0
    for ;i<len(leftPart) && j<len(rightPart);{
        if (leftPart[i] <=rightPart[j]){
            res =append(res,leftPart[i])
            i++
        }else{
            res = append(res,rightPart[j])
            j++
        }
    }
    for ;i<len(leftPart);i++{
        res=append(res,leftPart[i])
    }
    for ; j<len(rightPart); j++ {
        res =append(res, rightPart[j])
    }
    
    return res 
}


// 以下为单元测试  
// 

func main() {
    test:= [] int{1,2,3,4,5,9,7,5,1,0,4,55,6,8,77,558,6654,131,4,1,32,45,1,54654}
    // 一维向量

    fmt.Println(normalize(test))
}