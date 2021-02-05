package main
import "fmt"

type ListNode struct {
    Val int
    Next *ListNode
}

func RemoveNthNode(head *ListNode, n int) *ListNode{
    dummy := new (ListNode)
    dummy.Next =head
    cur_node := dummy
    fast_node := dummy
    if head ==nil {
        return nil
    }
    for i:=n;i>0;i--{
        fast_node =fast_node.Next
    }
    
    for fast_node.Next!=nil{
        cur_node =cur_node.Next
        fast_node =fast_node.Next
    }
    cur_node.Next =cur_node.Next.Next
    return dummy.Next
}

// test_data 0->1->2->3->4
// just for unit test
func main() {
    root :=&ListNode{}   
    leaf1 :=&ListNode{}
    leaf2 :=&ListNode{}
    leaf3 :=&ListNode{}
    leaf4 :=&ListNode{}

    leaf1.Val = 1
    leaf2.Val = 2
    leaf3.Val = 3
    leaf4.Val = 4
    root.Next = leaf1
    leaf1.Next =leaf2
    leaf2.Next =leaf3
    leaf3.Next =leaf4

    temp :=root
    for temp !=nil {
        fmt.Println("val:...",temp.Val)
        temp = temp.Next
    }
    temp1 := RemoveNthNode(root,2)
    if temp1== nil{
        fmt.Println("some error happen")
    }
    for temp1 !=nil {
        fmt.Println("revise_val:...",temp1.Val)
        temp1 = temp1.Next
    }
}