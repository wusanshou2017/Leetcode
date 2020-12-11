package main
import (
    "fmt"
    "sort"
)
// for i := 0; i < OUTER_COUNT; i++ {
//             sl := make([]string,0,INNER_COUNT)
//             for j := 0; j < INNER_COUNT; j++ {
//                 sl = append(sl,"a")
//             }
//             s = append(s,sl)
//         }
//         fmt.Println(s)
//
//dic_for_sum
//scoreMap := make(map[string]int, 8)
func cantains(nums[] int,t int ) bool{
    for _, v:= range nums{
        if (t==v){
            return true
        }
    }
    return false
}

func three_sum(nums[] int,target int) int{
    sort.Ints(nums)
    var res[][] int
    dic_sum_index := make(map[int] []int,0)
    n = len(nums)
    // loop for creat the map
    for i:=0;i<n-1;i++{
        for j:=i+1;j<n;j++{
            var index_temp =[...]int {i,j}
            dic_sum_index[nums[i]+nums[j]] = index_temp
        }
    }
    
    for i:=0;i<n;i++{
         _, flag := dic_sum_index[target-nums[i]]
         if (flag){
            temp_arr:= dic_sum_index[target-nums[i]]
            for _, v := range temp_arr{
                if (i==v){
                    break
                }

            }


         }


    }
    
    


}

func main() {

    
}

