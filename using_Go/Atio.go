package main

import (
    "fmt" 
)

var dfa = make (map[string] []string)
var nums_table = make(map[string] int)
var state string
var ans int 
var sign int
var INT_MAX int
var INT_MIN int
func get_col(c string)int{
    if (c==" ") {return 0}
	if (c=="+" || c =="-") {return 1}
	if (c>="0" && c<="9") {return 2}
	return 3
}

func get(c string){
    state = dfa[state][get_col(c)]
    if (state=="in_num"){
        temp:= nums_table[c]
        ans=ans*10 + temp
        if (ans>INT_MAX){ans=INT_MAX}
        if (ans<INT_MIN){ans =INT_MIN}
    }
    if (state=="signed"){
        if (c=="+"){
            sign=1
        }
        if(c=="-"){
            sign=-1
        }
    }
}
func myAtoi(s string) int {
    dfa["start"] = []string{"start","signed","in_num","end"}
    dfa["signed"] = []string{"end","end","in_num","end"}
    dfa["in_num"] = []string{"end","end","in_num","end"}
    dfa["end"] = []string{"end","end","end","end"}
    nums_table["1"]=1
    nums_table["2"]=2
    nums_table["3"]=3
    nums_table["4"]=4
    nums_table["5"]=5
    nums_table["6"]=6
    nums_table["7"]=7
    nums_table["8"]=8
    nums_table["9"]=9
    nums_table["0"]=0
    state="start"
    ans =0
    sign =1
    INT_MIN = -2147483648  //2**31-1 
    INT_MAX = 2147483647   // -2**31
    for _,c :=range s{
        get(string(c))
    }
    if ((sign*ans)<INT_MIN){return INT_MIN}
    if ((sign*ans)>INT_MAX) {return INT_MAX}
    return sign*ans
}

// test_case 
// "  +45646 wsdff"
// "weee 45456"
// "fff  444"
func main() {
    res:= myAtoi("   -4df4 somebad")
    fmt.Println(res)
}