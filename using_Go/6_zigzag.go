package convert

import(
    "strings"
)

func convert(s string, numRows int) string {
    if (numRows<2){return s}
    res  := make([]string,numRows)
    i:=0
    flag :=-1
    for _,c:=range s{
        res[i]+=string(c)
        if (i==0 || i ==numRows-1){flag=-flag}
        i+=flag
    }
    return strings.Join(res,"")
}