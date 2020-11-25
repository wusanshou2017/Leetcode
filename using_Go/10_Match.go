package main

import (   
    "fmt" 
)

func match(s string, p string) bool {

    m = len(s)
    n = len(p)
    var matrix  [m][n] bool
    for i:=0; i<m+1;i++{
        for j:=0; j<n+1;j++{
            matrix[i][j]=false
        }
    }
    matrix[0][0] =true
    for i:=0; i<m+1;i++{
        for j:=0; j<n+1;j++{
            if (p[i-1]=="*"){
                matrix[i][j] |= matrix[i-2][j]
                if ((p[i-2]==s[i-1] || p[i-2]==".") && ) 
                    matrix[i][j] |= matrix[i-2][j]
            }else{
                matrix[i][j] = (p[i-1]==s[j-1] or p[i-1] == ".")
            }
        }
    }

    return matrix[m][n]
}

// func main() {

    
// }