#include <iostream>
#include <vector>
using namespace std;
class Solution
{
public:
    bool isMatched(string s,string p)
    {
        vector<vector <bool>> dp(s.size()+1,vector<bool>(p.size()+1, false));
        dp[0][0]= true;
        for (int i=0;i<=s.size();++i)
        {
            for (int j = 1; j <= p.size(); ++j)
            {
                if (j > 1 && p[j - 1] == '*')
                {
                    dp[i][j] = dp[i][j - 2] || (i > 0 && (s[i - 1] == p[j - 2] || p[j - 2] == '.') && dp[i - 1][j]);
                }
                else
                {
                    dp[i][j] = i > 0 && ((p[j - 1] == s[i - 1]) || p[j - 1] == '.') && dp[i - 1][j - 1];
                }
            }
        }

        return dp[s.size()][p.size()];
    }



};
int main()

{
    string s1("abc");
    string s2("abc");
    Solution solution;
    if(solution.isMatched(s1,s2))
    std::cout << "Hello, World!" << std::endl;
    cout<<"finish"<<endl;
    return 0;
}