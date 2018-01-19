# Leetcode: Remove Nth Node From End of List     :BLOG:Basic:


---

Remove Nth Node From End of List  

---

Given a linked list, remove the nth node from the end of list and return its head.  

For example,  

Given linked list: 1->2->3->4->5, and n = 2.  

After removing the second node from the end, the linked list becomes 1->2->3->5.  

Note:  
-   Given n will always be valid.
-   Try to do this in one pass.

Blog link: <http://brain.dennyzhang.com/remove-nth-node-from-end-of-list>  

Github: challenges-leetcode-interesting  

Credits To: leetcode.com  

Leave me comments, if you know how to solve.  

    ## Basic Ideas: Two pointers with distance of n+1
    ##              Since the head node might be deleted, we need a dummy node
    ##              One pass
    ##              1->2->3->4->5, n=2
    ##                    p  .  . q
    ##
    ##   Assumption: If n is bigger than the length of the list, do nothing
    ## Complexity: Time O(n), Space O(1)
    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def removeNthFromEnd(self, head, n):
            """
            :type head: ListNode
            :type n: int
            :rtype: ListNode
            """
            dummyNode = ListNode(None)
            dummyNode.next = head
            p, q = dummyNode, dummyNode
            for i in xrange(n+1):
                q = q.next
            while q:
                p = p.next
                q = q.next
            p.next = p.next.next
            return dummyNode.next