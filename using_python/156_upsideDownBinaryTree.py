# Definition for a binary tree node.



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        


def deal_with_file(file_name:str):
    f = open(file_name,"r",encoding="utf-8")
    all_lines = f.readlines()
    all_lines =[ line.strip() for line in all_lines]
    return [ [float(char)for char in line.split(",")] for line in all_lines]
    
import os

def get_bgr(prefix:str,file_dir:str):
    # 获取路径下 所有的文件名
    res = []
    # _,_,file_name_lst = os.walk(file_dir)
    for  _,_,file in os.walk(file_dir):
        if file.startswith(prefix):
            nums_lst = deal_with_file(file)
            res.append(nums_lst)
    return res





