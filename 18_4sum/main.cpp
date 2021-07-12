#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
class Solution
{
public:
    vector<int > four_sum(vector<int > target)
    {
        sort(target.begin(),target.end());
        int n=target.size();
        if (n==0)
            return {};
        for (int i=0;i<n;i++)
        {
            int cur_sum=-target[i];





        }

    }






};
int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}