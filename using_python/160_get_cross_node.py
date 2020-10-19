# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> ListNode:
    	dummy2 =headB
    	while dummy2:
    		dummy1 = headA 
    		while dummy1:
    			if dummy1!=dummy2:
    				dummy1=dummy1.next
    			else:
    				return dummy1

    		dummy2=dummy2.next

    def getIntersectionNode2(self,headA:ListNode,headB:ListNode)->ListNode:
    	dummy1=headA
    	dummy2 = headB
    	l=[]
    	while dummy1:
    		l.append(dummy1)
    		dummy1=dummy1.next

    	while dummy2:
    		if dummy2 in l:
    			return dummy2
    		else:
    			dummy2=dummy2.next 
    	return None


    def getIntersectionNode(self,headA:ListNode,headB:ListNode)->ListNode:
       	dummy1 = headA
       	dummy2 = headB
       	while dummy1!=dummy2:
       		dummy1 = dummy1.next if dummy1 else headB
       		dummy2 = dummy2.next if dummy2 else headA

       	return dummy1

