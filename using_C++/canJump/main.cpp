#include <iostream>
#include <vector>
using namespace std;
class Solution{
public:
    bool canJump(vector<int> nums){

        int n = nums.size();
        int greedy = 0;
        for (int i=0;i<n;i++){
            if (i<=greedy){
                greedy= max(greedy,nums[i]+i);
                if (greedy >=n-1) return true;
            }

        }
        return false;
    }


};
int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}