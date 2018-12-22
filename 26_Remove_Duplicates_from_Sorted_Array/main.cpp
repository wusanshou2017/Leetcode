#include <iostream>
#include<vector>
using namespace std;
class Solution
{
public:
    
   int removeDuplicates(vector<int> &nums)
    {
        nums.erase(unique(nums.begin(),nums.end()),nums.end());
        return nums.size();
    }
    int removeDuplicates2(vector<int> &nums)
    {
        int i=0,j=1;
        while(j < nums.size())
        {
            if (nums[i] != nums[j])
            {
                nums[++i] = nums[j];
            }
            j++;

        }
        return i+1;
    }

};
int main()
{   vector<int> vec{1,2,3,3,4,4};
    Solution solution;
    cout<<solution.removeDuplicates(vec);
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
