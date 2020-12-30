#include <iostream>
#include <vector>
#include <algorithm>
# include<math.h>
using  namespace std;
static auto func =[](){
    ios::sync_with_stdio(false);
    cin.tie(0);
    return 0;
};

class Solution{
public:
    int findClosestNum (vector<int> nums,int target){
        int n = nums.size();
        sort(nums.begin(),nums.end());
        int res;
        if (n<3) return {};
        int diff = INT32_MAX;
        for (int i=0;i<n-2;i++){

            int l = i+1;
            int r = n-1;
            while (l<r){
                int sum = nums[i] +nums[l]+nums[r];
                if (abs(sum-target)<diff) {
                    diff = abs(sum-target);
                    res = sum;
                }
                if (sum<target) {
                    l++;
                }
                if (sum>target){
                    r--;
                }
                if (sum==target) return sum;
            }
        }
        return res;
    }
};

// unit test
int main() {
    Solution so;
    vector<int> test{-1,2,1,-4};
    int target = 1;
    auto ans = so.findClosestNum(test,target);
    cout<<ans<<endl;
    std::cout << "Hello, World!" << std::endl;
    return 0;
}