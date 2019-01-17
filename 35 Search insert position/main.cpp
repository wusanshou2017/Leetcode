#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    int searchInsert(vector<int>& nums, int target)
    {
        vector<int>::iterator iter1 = nums.begin();
        vector<int>::iterator iter2 =nums.begin()+1;
        if(target<nums[0])
        {
            nums.insert(nums.begin(),target);
            return 0;

        }
        if(target>nums[nums.size()-1])
        {
            nums.push_back(target);
            return nums.size()-1;
        }
        if(target>=nums[0]&&target<=nums[nums.size()-1])
        {
            int count=0;
            for (; iter2 != nums.end(); iter1++, iter2++)
            {
                count++;
                if(*iter1==target)
                {
                    nums.insert(iter1,target);
                    count--;
                    break;
                }
                if (*iter1 < target && *iter2 > target)
                {
                    nums.insert(iter2, target);
                    break;
                }

            }
            return count;
        }

    }



};


int main()
{
    Solution solution;
    vector<int> myVec={1,3,5,6};
    cout<<solution.searchInsert(myVec,4);
    for(auto i:myVec)
        cout<<i<<endl;
    std::cout << "Hello, World!" << std::endl;
    return 0;
}