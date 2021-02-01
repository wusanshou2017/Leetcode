/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
package main

type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}

func helper( left int ,right int , nums[] int) *TreeNode{
    if left>right{
        return nil
    }
    mid := (left +right)/2
    root := new(TreeNode)
    root.Val =nums[mid]
    root.Left = helper(left, mid-1, nums)
    root.Right = helper(mid+1, right, nums)
    return root  
}

func sortedArrayToBST(nums []int) *TreeNode {
    return helper(0, len(nums)-1, nums)
}


func main() {
    
}

