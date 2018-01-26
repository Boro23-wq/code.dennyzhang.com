# Leetcode: Reverse Linked List II     :BLOG:Basic:


---

Reverse a linked list from position m to n.  

---

Reverse a linked list from position m to n. Do it in-place and in one-pass.  

For example:  
Given 1->2->3->4->5->NULL, m = 2 and n = 4,  

return 1->4->3->2->5->NULL.  

Note:  
Given m, n satisfy the following condition:  
1 <= m <= n <= length of list.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/reverse-linked-list-ii)  

Credits To: [leetcode.com](https://leetcode.com/problems/reverse-linked-list-ii/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/reverse-linked-list-ii
    ## Basic Ideas: Insert to a given pointer for (n-m) times.
    ##       1. Change in the head, thus we need a dummy head node
    ##       2. Need to track get previous node of sub list
    ##       3. Need to track the head of original sub list
    ##       4. How many times each loop shall compute
    ## Complexity: Time O(n), Space O(1)
    ## Sample Data
    ##      1->2->3->4->5->6->NULL, m = 2 and n = 5
    ##         .  .  .  .
    ##      p     q  r
    ##
    ##      1->2->3->4->5->NULL, m = 1 and n = 3
    ##      .  .  .
    ##      p
    ##
    ##      3->5
    ##     dummy -> 3 -> 5
    ##       p
    ##              q     r
    ##     dummy -> 1 -> 2 -> 3
    ##       p      q    r
    
    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def reverseBetween(self, head, m, n):
            """
            :type head: ListNode
            :type m: int
            :type n: int
            :rtype: ListNode
            """
            # Nothing changed
            if m == n:
                return head
            dummyNode = ListNode(0)
            dummyNode.next = head
            p = dummyNode
            # p: points to the previous node of the sublist head
            for i in xrange(m-1):
                p = p.next
            # r points to current node
            # q points to the original first node of the sublist
            # No need to reverse the first node
            q = p.next
            r = q.next
            for i in xrange(n-m):
                q.next = r.next
                r.next = p.next
                p.next = r
                r = q.next
            return dummyNode.next