#include <iostream>
#include<vector>
#include<iterator>
#include <algorithm>
using namespace std;
class Solution
{
public:
    vector<vector<int >> threesum(vector<int>&nums)
    {
        vector<vector<int >> result;
        sort(nums.begin(),nums.end());
        vector<int>::iterator it1=nums.begin();
        vector<int>::iterator it2=nums.end();
        while(*it1!=*it2)
        {
            if((*it1+*it2)<0)
            {



            }



        }



    }



};
int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}