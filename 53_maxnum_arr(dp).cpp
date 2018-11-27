#include <iostream>
#include <vector>
using namespace std;
class Solution
{
public:
    int maxSubArray(vector<int> &nums)
    {
        int ret=nums[0];
        int prefix=0;
        if(nums.size()==1)
            return ret;
        if (nums.size()>1)
        {
            for(int i=0;i<nums.size();i++)
            {
                prefix=max(0,prefix);
                prefix+=nums[i];
                if (prefix>ret) ret=prefix;
            }

            return  ret;
        }

    }


};
int main()
{
    Solution solution;
    vector<int> nums{1,-3,4,6,5,-6};
    cout<<solution.maxSubArray(nums)<<endl;
    std::cout << "Hello, World!" << std::endl;
    return 0;
}