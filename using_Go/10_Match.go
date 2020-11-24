package main

import (   
    "fmt" 
)

func match(s string, p string) {

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


            }else{


            }
        }
    }

    return matrix[m][n]
}

func main() {

    
}