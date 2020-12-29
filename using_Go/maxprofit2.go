package main
import (
    "fmt"
)


func maxProfit(prices []int) int {
    n := len(prices)
    if n<2{
        return 0
    }
    var res int
    low_price := prices[0]
    for _, v :=range prices[1:]{
        if low_price< v{
            res += v-low_price
            low_price = v 
        }else{
            low_price = v
        }
    }
    return res
}


//  unit test [3, 1, 5, 7, 2, 3, 5, 7, 8, 1, 3]
func main(){
    test := []int{3, 1, 5, 7, 2, 3, 5, 7, 8, 1, 3}
    fmt.Println(maxProfit(test))

}