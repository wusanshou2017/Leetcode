#include <iostream>
#include<string>
using namespace std;
class Solution
{
public:
    int strStr(string haystack, string needle)
    {
        int m=haystack.size();
        int n=needle.size();
        int ans=-1;
        int temp=0;
        if(haystack.empty()&&needle.empty()) // edge solution
        {
            return 0;
        }
        for(int j=0;j<m;++j)
        {
            if(haystack[j]==needle[0])
            {
                ans=0;
                temp=j;
                break;
            }
            if(j==m-1). // edge solution
                return -1;
        }
        for(int i=0;i<n;++i)
        {
            if(haystack[temp+i]==needle[i])
            {
                ans++;
            }
            else ans=-1;
        }
        return ans;
    }
};
int main()
{
    Solution solution;
    cout<<solution.strStr("hello","ll");
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
