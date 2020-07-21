#include <iostream>
#include <string>
#include <vector>
using namespace  std;
class Solution{
public:
    bool isInterleave(string s1,string s2,string s3){
        int m = s1.size();
        int n = s2.size();

        vector<vector<bool>> dp ( m+1,vector<bool> (n+1, false));
        dp[0][0] = true;

        for (int i=1;i<m+1;i++){
            dp[i][0]= (dp[i-1][0] &&(s2[i-1]==s3[i-1]));
        }

        for (int j=1; j<n+1;j++){
            dp[0][j] = (dp[0][j-1] &&(s1[j-1]==s3[j-1]));
        }

        for (int i = 1; i<m+1;i++ ){
            for (int j= 1;  j<n+1;j++){
                dp[i][j] =  (dp[i-1][j]&&(s3[i+j-1] ==s2[i-1]))
                            or (dp[i][j-1]&&(s3[i+j-1]==s1[j-1]));
            }
        }
        return dp[m][n];
    }
};
int main() {
    Solution so;
    string s1 ="aabcc";
    string s2 ="dbbca";
    string s3= "aadbbcbcac";
    std::cout<<so.isInterleave(s1,s2,s3);
    std::cout << "Hello, World!" << std::endl;
    return 0;
}