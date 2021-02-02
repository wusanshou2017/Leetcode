package main

type TreeNode struct {
     Val int
     Left *TreeNode
     Right *TreeNode
 }

func isSameTree(p *TreeNode, q *TreeNode) bool {
    res :=helper( p, q)
    return res
}

func helper( r1 *TreeNode, r2 *TreeNode) bool{
    if r1 ==nil && r2 ==nil {return true }
    if r1 ==nil || r2 ==nil {return false}
    return r1.Val ==r2.Val && helper(r1.Left, r2.Left) && helper(r1.Right,r2.Right)   
}
func main() {
   
}


