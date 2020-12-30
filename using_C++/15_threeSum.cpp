#include <iostream>
#include <vector>
#include <algorithm>
using  namespace std;
static auto _=[]()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    return 0;
}();
class Solution{
public:
    vector<vector<int>> XSum(vector<int> nums){
        int n = nums.size();
        if (n<3){return {};}
        sort(nums.begin(),nums.end());
        vector <vector<int>> res{};
        for(int i=0;i<n;i++){
            if (i>0 and nums[i]==nums[i-1]) continue;
            int k = n-1;
            int target = 0- nums[i];
            for (int j=i+1;j<n;j++){
                if (j>i+1 and nums[j]==nums[j-1]) continue;
                while  (j<k and (nums[j]+nums[k])>target) k--;
                if (j ==k) break;
                if ((nums[j] + nums[k])==target){
                    vector<int> one_ans {nums[i],nums[j],nums[k]};
                    res.push_back(one_ans);
                }
            }
        }
        return res;
    }
};
int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}