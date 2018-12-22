#include <iostream>
#include<vector>
using namespace std;
class Solution
{
public:
   int removeDuplicates(vector<int> &nums)
   {
       int i=0,j=1;
       if(nums.size()<2)
        return 0;
       int count=0;
       while(i<nums.size())
       {

           if(nums[i]!=nums[j])
           {
               count++;
               i=j;
               j++;
           }
           if(nums[i]==nums[j])
           {
               j++;
           }

       }
        return count;

   }


};
int main()
{   vector<int> vec{1,2,3,3,4,4};
    Solution solution;
    cout<<solution.removeDuplicates(vec);
    std::cout << "Hello, World!" << std::endl;
    return 0;
}