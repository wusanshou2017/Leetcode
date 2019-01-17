#include <iostream>
#include<vector>
using namespace std;
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        return lower_bound(nums,target);
    }

    int lower_bound(vector<int>& nums,int target){
        int low=0,high=nums.size()-1;

        while(low<=high){
            int mid=(low+high)>>1;
            if(nums[mid]<target)
                low=mid+1;
            else
                high=mid-1;
        }
        return low;
    }
};

int main()
{
    vector<int> my_vec={2,3,5,6,9};
    Solution solution;
    cout<<solution.searchInsert(my_vec,6);

    std::cout << "Hello, World!" << std::endl;
    return 0;
}