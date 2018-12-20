#include <iostream>
using namespace std;
struct ListNode
{
    int val;
    ListNode* next;
    ListNode(int x):val(x), next(NULL){};
};
class Solution
{
public:
    ListNode* swap_nodes(ListNode*head) {
        ListNode *A = head;
        ListNode *B = head->next;
        ListNode *pre = NULL;
        head = head->next;
        while (B) {
            A->next = B->next;
            B->next = A;
            if (pre)
                pre->next = B;
            pre = A;
            A = A->next;
            if (!A)
                break;
            B = A->next;
        }


        return head;
    }

};
int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}