# Leetcode: Reorder List     :BLOG:Medium:


---

Reorder List  

---

Given a singly linked list L: L0 -> L1 -> &#x2026; -> Ln-1 -> Ln,  
reorder it to: L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> &#x2026;  

You must do this in-place without altering the nodes' values.  

For example,  
Given {1,2,3,4}, reorder it to {1,4,2,3}.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/reorder-list)  

Credits To: [leetcode.com](https://leetcode.com/problems/reorder-list/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/reorder-list
    ## Basic Ideas:
    ##             Find the right sub-list after n/2 node
    ##             Reverse the right sub-list
    ##             Insert it into the sub-list one by one
    ## Complexity: Time O(n), Space O(1)
    ##
    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def reorderList(self, head):
            """
            :type head: ListNode
            :rtype: void Do not return anything, modify head in-place instead.
            """
            if head is None or head.next is None or head.next.next is None:
                return
    
            length = 0
            p = head
            while p:
                length += 1
                p = p.next
            p = head
            for i in xrange(length/2):
                p = p.next
    
            # reverse sub-list after p
            q = p.next
            p.next = None
            while q:
                r = q.next
                q.next = p.next
                p.next = q
                q = r
    
            # insert the right-sub list to the left-sub list
            p1 = head
            p2 = p.next
            p.next = None
    
            while p2:
                r = p2.next
                p2.next = p1.next
                p1.next = p2
                p1 = p1.next.next
                p2 = r