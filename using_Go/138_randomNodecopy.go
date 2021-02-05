package main

import (
    "fmt"
)

type Node struct {
    // define the Node
    Val interface{}
    Next *Node
    Random *Node
}

func getCloneNode(visitedMap map[*Node] *Node, p *Node) *Node{
    if v, ok := visitedMap[p];ok{
        return v
    }else{
        var v* Node
        if p != nil{
            v= &Node{p.Val,nil,nil}
        }
        visitedMap[p]= v
        return v
    }
}

func copyRandomList(head *Node) *Node{
    if head ==nil{
        return nil
    }
    visitedMap:= make(map[*Node]*Node)
    oldNode := head
    newNode := getCloneNode( visitedMap,oldNode)
    newHead := newNode
    for oldNode != nil{
        newNode.Next = getCloneNode(visitedMap, oldNode.Next)
        newNode.Random = getCloneNode(visitedMap, oldNode.Random)
        oldNode = oldNode.Next
        newNode = newNode.Next
    }
    return newHead
}

// unit test 
// data 1 [2]->2 [self] ->None


func main() {
    // generate test data
    node1 :=&Node{}
    node2 :=&Node{}
    node1.Val = 1
    node1.Next =node2
    node2.Val = 2
    node2.Next =nil
    node1.Random =node2
    node2.Random = node1
    res:= copyRandomList( node1)
    temp1 := res
    for temp1!=nil{
        fmt.Println("next 域:...",temp1.Val)
        temp1 =temp1.Next
    }
    
    temp2 := res 
    for temp2!=nil{
        fmt.Println("random 域:...",temp2.Val)
        temp2=temp2.Random
    }
}