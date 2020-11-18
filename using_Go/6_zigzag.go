<<<<<<< HEAD
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

=======
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
>>>>>>> a60f2c8891f7d6d14ae6abb14b44959986b26e82
}