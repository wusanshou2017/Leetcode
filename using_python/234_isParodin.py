# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # def isPalindrome(self, head: ListNode) -> bool:
    #     res =[]
       
    #     while head:
    #         res.append(head.val)
    #         head =head.next 
        
    #     return res ==res[::-1]
        
    def isPalindrome(self,head:ListNode)-> bool:

        n,mid = 0 , 0
        dummy = head
        while dummy:
            dummy = dummy.next
            n+=1
        l1 =[]
        l2 =[]
        # 对n 的值进行校验
        if n%2==0:
            mid = n//2
            dummy1= head
            dummy2 =head
            while mid>0:
                dummy2 =dummy2.next
                mid -=1
            
            while dummy2:
                l1.append(dummy1)
                l2.append(dummy2)
                dummy1=dummy1.next
                dummy2 = dummy2.next
                
                
           

        else:
            mid = n//2
            dummy1 =head 
            dummy2 = head
            while mid>0:
                dummy2 = dummy2.next
                mid -=1

            while dummy2:
                l1.append(dummy1)
                l2.append(dummy2)
                dummy1=dummy1.next
                dummy2 = dummy2.next

        return l1[::-1]==l2[:]
            

if __name__ == '__main__':
    head =  ListNode(0)
    head2 = ListNode(0)
    head3 = ListNode(1)
    head4 = ListNode(1)

    head.next  = head3
    # head2.next =head3
    head3.next = head4
    head4.next = head2 
    so =Solution()
    print (so.isPalindrome(head))