func isMatch(s string, p string) bool {
    m := len(s)
    n := len(p)
    matrix := make([][]bool, m + 1)
    for i := 0; i < len(matrix); i++ {
        matrix[i] = make([]bool, n + 1)
    }

    matrix[0][0] =true
    for i:=0; i<=m;i++{
        for j:=1; j<=n;j++{
            if (p[j-1]=='*'){
                matrix[i][j] =matrix[i][j] || matrix[i][j-2]
                if ((i>0)&&((p[j-2]==s[i-1] || p[j-2]=='.'))) {
                    matrix[i][j] = matrix[i][j]||matrix[i-1][j]
                }
            }else if ((i>0)&&((p[j-1]==s[i-1]) || (p[j-1] == '.'))){
                matrix[i][j] = matrix[i][j] ||                      matrix[i-1][j-1]
            }
        }
    }

    return matrix[m][n]

}