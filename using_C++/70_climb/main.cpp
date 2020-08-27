#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int climbStairs(int n) {
        vector<int > dp (0,n);
        if (n==1) return 1;
        if (n==2) return 2;
        dp[0]=1;
        dp[1]=2;
        for(int i =2;i<n;i++){
            dp[i]=dp[i-1]+dp[i-2];
        }
        return dp[n];
    }
};

int main() {
    Solution so;
    std::cout<<so.climbStairs(7)<<std::endl;
    std::cout << "Hello, World!" << std::endl;
    return 0;
}