package main

import (
    "fmt"
    "os"
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
            v= &Node{p.val,nil,nil}
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
        newNode.next =getCloneNode(visitedMap, oldNode.Next)
        newNode.Random = getCloneNode(visitedMap, oldNode.Random)
        oldNode = oldNode.Next
        newNode = newNode.Next
    }
    return newHead
}
