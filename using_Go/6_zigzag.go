package zigzag
import "fmt"

func zigzag(s string ,numRows int) string {
    if (numRows<2) {return s}
    var res [numRows] string
    i:=0
    flag:= -1
    for j := 0; j <len(s); j++ {
        res[i]+=s[j]
        if (i==0 || i ==numRows-1){
            flag = -flag
        }
        i+=flag
    }
    return strings.Join(res, "")

}