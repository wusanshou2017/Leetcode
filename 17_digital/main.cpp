#include <iostream>
#include <string>
#include <vector>
using namespace std;
class Solution {
public:
    vector<string> tab={"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    vector<string> letterCombinations(string digits) {
        if(digits.size()==0)return {};
        vector<string> res;
        string path;
        int len=digits.size();
        dfs(res,digits,0,path);
        return res;
    }
    void dfs(vector<string>& res,string digits,int di,string path)
    {
        if(di==digits.size())
        {
            res.push_back(path);
        }else
        {
            int num=digits[di]-'0';
            for(int ti=0;ti<tab[num].size();ti++)
            {
                path.push_back(tab[num][ti]);
                di++;
                dfs(res,digits,di,path);
                di--;
                path.pop_back();
            }
        }
    }
};


int main() {
    Solution so;
    vector<string> res =so.letterCombinations("234");
    for (auto s:res){
        cout<<s<<endl;
    }
    std::cout << "Hello, World!" << std::endl;
    return 0;
}