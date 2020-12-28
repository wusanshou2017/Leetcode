package main
import "fmt"

type ListNode struct {
    Val int
    Next *ListNode
}

func hasCycle(head *ListNode,x int) bool {
    dummy1 :=  &ListNode{}
    dummy2 := &ListNode{}
    head1 :=dummy1
    head2 := dummy2
    for head1!=nil && head2!=nil{
        if head1.val!= head2.val{
            head1 =head1.Next
            head2 = head2.Next.Next
        }else{
            return true
        }
    } 
    return false
    
}
func main() {
    
    
}