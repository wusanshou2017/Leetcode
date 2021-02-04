# Definition for singly-linked list.
#
#     You are appreciated...
# 　　When i was young, me and my mama had beef
# 　　17 years old kicked out on tha streets
# 　　Though back in tha time, i never thought i'd see her face
# 　　Ain't a woman alive that can take my momma's place
# 　　Suspended from school, scared ta go home
# 　　I was a fool with tha big boys breaking all tha rules
# 　　Shed tears with my baby sister
# 　　Over tha years we wuz poorer than tha other little kids
# 　　And even though we had different daddies
# 　　Tha same drama when things went wrong we blamed mama
# 　　I reminised on tha stress i caused, it wuz hell
# 　　Hugg'en on my mama from a jail cell
# 　　And who'ed think in elementary, heeeey i'd see tha penitentiary
# 　　One day
# 　　Running from tha police, that's right
# 　　Momma catch me--put a whoop'en to my backside
# 　　And even as a crack fiend mama,
# 　　Ya always was a black queen mama
# 　　I finally understand for a woman
# 　　It ain't easy--trying ta raise a man
# 　　Ya always wuz commited, a poor single mother on welfare,
# 　　Tell me how ya did it
# 　　There's no way i can pay ya back
# 　　But tha plan is ta show ya that i understand.
# 　　You are appreciated......
# 　　Laaaaady, don't cha know we luv ya
# 　　Sweeeet laaaady, place no one above ya
# 　　Sweeeet laaaady, don't cha know we luv ya
# 　　Ain't nobody tell us it wuz fair
# 　　No luv for my daddy, cause tha coward wuzn't there
# 　　He passed away and i didn't cry
# 　　Cause my anger, wouldn't let me feel for a stranger
# 　　They say i'm wrong and i'm heartless
# 　　But all along i wuz looking for a father--he wuz gone
# 　　I hung around with tha thug's and even though they sold drugs
# 　　They showed a young brother luv
# 　　I moved out and started really hang'in
# 　　I needed money of my own so i started slang'in
# 　　I ain't guilty cause, even though i sell rocks
# 　　It feels good, putting money in your mailbox
# 　　I love paying rent when tha rents due
# 　　I hope ya got tha diamond necklace that i sent to you
# 　　Cause when i wuz low, you was there for me
# 　　Ya never left me alone, cause ya cared for me
# 　　And i can see ya coming home after work late
# 　　Ya in tha kitchen trying ta fix us a hot plate
# 　　Just working with tha scraps you wuz given
# 　　And mama made miracles every thanksgiving
# 　　But now tha road got rough, your alone
# 　　Trying ta raise two bad kids on your own
# 　　And there's no way i can pay ya back
# 　　But my plan is ta show ya that i understand
# 　　You are appreciated.....
# 　　Laaaaady, don't cha know we luv ya
# 　　Sweeeet laaaady, place no one above ya
# 　　Sweeeet laaaady, don't cha know we luv ya
# 　　Pour out some liquor and i remenise
# 　　Cause through tha drama, i can always depend on my mama
# 　　And when it seems that i'm hopeless
# 　　You say tha words that can get me back in focus
# 　　When i wuz sick as a little kid
# 　　Ta keep me happy theres no limit to tha things ya did
# 　　And all my childhood memories
# 　　Are full of all tha sweet things ya did for me
# 　　And even though i act craaaazy
# 　　I got ta thank tha lord that ya maaaade me
# 　　There are no words that can express how i feel
# 　　Ya never kept a secret, always stayed real
# 　　And i appreciate how ya raised me
# 　　And all tha extra love that ya gave me
# 　　I wish i could take tha pain away
# 　　If you can make it through tha night, there's a brighter day
# 　　Everything'll be alright if ya hold on
# 　　It's a struggle
# 　　Everyday gotta roll on
# 　　And there's no way i can pay ya back
# 　　But my plan is ta show ya that i understand
# 　　You are appreciated.......
# 　　Laaaaady, don't cha know we luv ya
# 　　Sweeeet laaaady, place no one above ya
# 　　Sweeeet laaaady, don't cha know we luv ya, sweeeet laaaady
# 　　Laaaady...
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        cur_node = dummy
        fast_node = dummy
        while n > 0:
            fast_node = fast_node.next
            n -= 1

        while fast_node.next:
            cur_node = cur_node.next
            fast_node = fast_node.next

        cur_node.next = cur_node.next.next

        return dummy.next


head = ListNode(0)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = None

so = Solution()


res = so.removeNthFromEnd(head, 2)
while res:

    print(res.val)
    res = res.next
