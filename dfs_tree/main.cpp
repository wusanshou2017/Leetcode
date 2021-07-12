#include <iostream>
#include <vector>
#include <string>
using namespace std;
class dfs_tree
{
public:
    vector<vector<string>> get_words(vector<vector<string>> target){
        if (target.size()==0)
            return {};
        vector <vector<string>> res;
        vector<string> path={};

        dfs(res,target,path,0);
        return res ;
    }
    void dfs(vector<vector<string>> &res,vector<vector<string>> target, vector<string> path,int depth)
    {
        if (depth==target.size())
        {
            res.push_back(path);
        }
        else{

            for (int i=0;i<target[depth].size();i++)
            {
                path.push_back(target[depth][i]);
                depth++;
                dfs(res,target,path,depth);
                path.pop_back();
                depth--;
                //dfs(res,target,path,nodes);
            }

        }
    }
    void bfs (vector<vector<string>> &res,vector<vector<string>> target, vector<string> path,int depth)
    {
        if



    }



};
int main() {
    vector<vector<string >> target{{"pre","com","re"},{"a1","a2","a3"},{"b1","b2","b3"},{"c1","c2","c3","c4"}};
    dfs_tree so;
    vector<vector<string> > res =so.get_words(target);
    for (auto vec: res )
        for (auto s:vec)
            cout<<s<<endl;
    std::cout << "Hello, World!" << std::endl;
    return 0;
}