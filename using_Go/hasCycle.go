package main
import "fmt"

type ListNode struct {
    Val int
    Next *ListNode
}

func hasCycle(head *ListNode,x int) bool {
    head1 := head
   
    if head1 ==nil || head1.Next==nil{
        return false
    }
   
    head2 := head1.Next

    for head1!=head2{
        if head2==nil || head2.Next==nil{
            return false
        }
        head1 = head1.Next
        head2 = head2.Next.Next

    }
    return false
    
}

func unit_test(head *ListNode,x int){
// to do 



}
func main() {
    // 
    fmt.Println("test...")

}