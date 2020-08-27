#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int climbStairs(int n) {
        
        if (n==1) return 1;
        if (n==2) return 2;
        int pre1 =1;
        int pre2 =2;
        int ans =1;
        for(int i =2;i<n;i++){
            ans =pre1+pre2;
            pre1 =pre2;
            per2 = ans;
        }
        return ans;
    }
};

int main() {
    Solution so;
    std::cout<<so.climbStairs(7)<<std::endl;
    std::cout << "Hello, World!" << std::endl;
    return 0;
}