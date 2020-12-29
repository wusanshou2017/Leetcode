package main
import "fmt"

func getmin(strs[] string) string{
    var minIndex int
    temp_len := len(strs[0])
    for index, s:=range(strs){
        if len(s)<temp_len{
            minIndex = index
        }
    }
    return strs[minIndex]
}

func longestCommonPrefix(strs[]string ) string{
    if len(strs)==0{
        return ""
    }
    if len(strs)==1{
        return strs[0]
    }
    min_str := getmin(strs)
    for index, c:=  range min_str{
        for _,s:=range strs{
            if s[index]!=byte(c){
                return min_str[:index]
            }
        }
    }
    return min_str
}

//  unit_test
func main() {
    var test =[]string {"","app","apple"}
    
    fmt.Println(longestCommonPrefix(test))
}
