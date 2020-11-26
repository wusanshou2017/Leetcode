func getMax(x,y int) int{
    if x>y{
        return x
    }
    return y
}

func maxArea(height []int) int {
    left:= 0
    right :=len(height)-1
    ans :=0
    for(left<right){
        if height[left]>height[right]{
            ans = getMax((right-left)*height[right],ans)
            right-=1
        }else{
            ans =getMax((right-left)*height[left],ans)
            left+=1
        }
    }
    return ans 
}