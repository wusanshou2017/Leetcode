#include <iostream>
#include<vector>
using namespace std;
class Solution
{
public:
    int removeElement(vector<int > &nums, int val ) const //测试不通过
    {
        int ans=0;
        for(int i=0;i<nums.size();++i)
        {
            if(nums[i]==val)
            {
                ans++;
                nums[i]=nums[nums.size()-1];
            }
        }
        return nums.size()-ans;

    }

    int removeElement2(vector<int>& nums, int val)  //通过测试
    {

        int ans=0;
        for(int i=0;i<nums.size();++i)
        {
            if(nums[i]!=val)
            {

                nums[ans]=nums[i];
                ans++;
            }
        }
        return ans;
    }
};
int main()

{
    Solution solution;
    vector<int> vec {3,2,2,3};
    cout<<solution.removeElement(vec,3);
    std::cout << "Hello, World!" << std::endl;
    return 0;
}