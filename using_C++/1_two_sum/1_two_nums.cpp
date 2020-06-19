#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;
class Solution
{
public:
    vector<int> twoSum(vector<int >& nums,int target)
    {unordered_map<int,int > m;
    vector<int> results;
    for (int i=0;i<nums.size();++i)

        {m[nums[i]]=i;}
        for (int i=0;i<nums.size();++i)
        {   int t=target-nums[i];
            if(m.count(t)&&m[t]!=i)
            {
                results.push_back(i);
                results.push_back(m[t]);
                break;
            }

        }
        return  results;
    }


};
int main()
{   Solution solution;
    vector<int> m_vec{2,7,11,15};
    vector<int >res=solution.twoSum(m_vec,18);
    for(auto c:res)
        cout<<c<<endl;
    std::cout << "Hello, World!" << std::endl;
    return 0;
}