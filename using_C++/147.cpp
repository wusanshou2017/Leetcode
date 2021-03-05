class ListNode{
public:
    ListNode(int value):val(value){}
    int val;
    ListNode * next =nullptr;
}

#define min_num -65535

class Solution {
public:
    ListNode* insertionSortList(ListNode* head) {
        dummy =new(ListNode(min_num));
        dummy.next = &head;
        auto sortedPtr = dummy;
        auto curPtr = sortedPtr.next;
        while (curPtr!=nullptr){
            auto temp =&dummy
            while temp!= sortedPtr.next{
                if (temp.val>curPtr.val){
                    swap(temp,curPtr);
                    sortedPtr = sortedPtr.next;
                }
                temp = temp.next;
            }
            curPtr= curPtr.next;
        }
    }
    void swap(ListNode *head1,ListNode *head2){
        auto temp =head1.val
        head1.val = head2.val
        head2.val =temp 
    }
};