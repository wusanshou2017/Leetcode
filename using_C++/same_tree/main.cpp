#include <iostream>
#include<vector>
using namespace std;

struct TreeNode{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode (int x ):val(x),left(NULL),right(NULL){}
};

class Solution{
public:
    bool JudgeSame (TreeNode *r1,TreeNode *r2){
        auto res =helper(r1,r2);
        return res;
    }

    bool helper (TreeNode *root1, TreeNode *root2){
        // 退出条件
        if (root1==NULL  and root2==NULL) return true;
        if (root1 ==NULL or root2==NULL) return false;
        return root1->val ==root2->val and helper(root1->left,root2->left) and
        helper(root1->right,root2->right);
    }
};


int main() {
    auto node1 =new TreeNode(5);
    auto node2 = new TreeNode(5);
    Solution so;
    cout<<so.JudgeSame(node1,node2)<<endl;
    std::cout << "Hello, World!" << std::endl;
    return 0;
}