#include <iostream>
#include <vector>
#include <string>
using  namespace std;
class Solution{
public:
    bool isMatch(std::string s,std::string p){
        int m = p.size();
        int n = s.size();
        vector<vector<bool>> dp (m+1, vector<bool>(n+1, false));
        dp[0][0]=true;
        for (int i =1;i<m+1;i++){
            if (p[i-1]=='*'){
                dp[i][0]=true;
            }
            else break;
        }
        for (int i=1;i<m+1;i++){
            for (int j=1;j<n+1;j++){
                if (p[i-1]=='*'){
                    dp[i][j] = dp[i-1][j] or dp[i][j-1];
                }
                else if (p[i-1]=='?'){
                    dp[i][j]= dp[i-1][j-1];
                }
                else{
                    dp[i][j] = (p[i-1]==s[j-1]) and (dp[i-1][j-1]);
                }
            }
        }
        return dp[m][n];
    }
};
int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}