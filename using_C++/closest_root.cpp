#include<iostream>
using namespace std;
void preorder(TreeNode *node, TreeNode *search){
    if(!node){
        return;
    }
    if(node == search){
        
    }
    preorder(node->left,search);
    preorder(node->right,search);
}
void preorder(TreeNode *node,TreeNode *search, std::vector<TreeNode*> &path,std::vector<TreeNode*> &result,int &finish)
{//node 正在遍历节点，search待搜索节点，path 遍历时节点路径栈，result 最终搜索到节点search的路径结果，finish 记录是否找到节点search的遍历，未找到时是0，找到为1{
    if(!node || finish){
    return;//当node为空或已找到search 节点直接返回，结束搜索
     }
    path.push_back(node);//先序遍历时，将节点压入path栈
    if(node == search){
        finish = 1;
        result = path;
    }
    preorder(node->left,search,path,result,finish);
    preorder(node->right,search,path,result,finish);
    path.pop_back();//结束遍历node时，将node节点弹出path栈

}

class Solution{
public:
    TreeNode* lowestCommonAncestor(TreeNode * root, TreeNode *p ,TreeNode *q){
        std::vector<TreeNode*> path;申明遍历用的临时栈
        std::vector<TreeNode*> node_p_path;//储存P节点路径
        std::vector<TreeNode*>node_q_path;//储存q节点路径
        int finish = 0;//记录是否完成搜索
        preorder(root, p,path,node_p_path,finish);
        path.clear();//清空path，finish,计算q节点路径
        finish = 0;
        preorder(root, q, path,node_q_path,finish);
        int path_len = 0;
        if(node_p_path.size() < node_q_path.size()){
            path_len = node_p_path.size();
        }
        else{
            path_len = node_q_path.size();
        }
        TreeNode * result = 0;
        for (int i = 0; i < path_len; i++){
            if(node_p_path[i] = node_q_path[i]){
                result = node_p_path[i];
            }//最后相同的节点为最近公共节点
        }
        return result;
}
};
