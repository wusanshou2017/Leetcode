#include <iostream>
#include <vector>
#include <string>
using namespace std;
class list_node{
public:
    list_node(int value):val(value){}
    int val;
    list_node *next=nullptr;
};
class solution{
public:
    list_node remove_node(list_node node, int n){
        int nums=1;
        list_node tmp=node;
        for (int i =0; i<n;i++){
            if (tmp.next!= nullptr)
            {
                tmp=*tmp.next;
                nums++;
            }
            else
                break;
        }
        if (nums<n)
        {
            return node;
        }
        nums = nums-n;
        tmp = node;
        for (int j=0;j<nums;j++)
        {
            tmp=*tmp.next;
        }

    }
};

void fun(int var){


    cout<<var<<endl;
}
int main() {
    list_node node1(1);
    list_node node2(2);
    list_node node3(3);
    node1.next=&node2;
    node2.next=&node3;
    cout<<node1.next->next->val;
}
