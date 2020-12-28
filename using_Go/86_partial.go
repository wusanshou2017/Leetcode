package partition
 // Definition for singly-linked list.
 
import "fmt"

type ListNode struct {
    Val int
    Next *ListNode
}



func partition(head *ListNode, x int) *ListNode {
    dummy1 :=&ListNode{}
    dummy2 :=&ListNode{}
    dummy1_head := dummy1
    dummy2_head :=dummy2
    for head!= nil{
        if head.Val<x{
            dummy1.Next=head
            dummy1 = dummy1.Next
        } else{
            dummy2.Next =head
            dummy2 = dummy2.Next
        }
        head = head.Next
    }

    dummy2.Next =nil 
    dummy1.Next = dummy2_head.Next
    return dummy1_head.Next
}

