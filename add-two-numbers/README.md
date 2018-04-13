# Leetcode: Add Two Numbers     :BLOG:Basic:


---

Add Two Numbers  

---

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.  

You may assume the two numbers do not contain any leading zero, except the number 0 itself.  

    Example
    
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/add-two-numbers)  

Credits To: [leetcode.com](https://leetcode.com/problems/add-two-numbers/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/add-two-numbers
    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def addTwoNumbers(self, l1, l2):
            """
            :type l1: ListNode
            :type l2: ListNode
            :rtype: ListNode
            """
            ## Idea:
            ##         Need to track the previous node
            ##         Take in-place change? Empty links?
            ## Complexity: Time O(n), Space O(1)
            ## Sample Data:
            ##  2 -> 4 -> 3
            ##  p    r
            ##  5 -> 6 -> 8 -> 9
            ##  q    s
            ##  One or two link are empty
            if l1 is None or l2 is None:
                return l1 if l2 is None else l2
    
            # add l2 to l1
            has_carry = False
            head = l1
            p, q = l1, l2
            r, s = p.next, q.next
            p.val += q.val
    
            if p.val >= 10:
                p.val = p.val % 10
                has_carry = True
    
            # merge 2 list
            while r and s:
                if has_carry is True:
                    r.val += 1
                    has_carry = False
                r.val += s.val
                if r.val >= 10:
                    has_carry = True
                    r.val = r.val % 10
                p, q = p.next, q.next
                r, s = p.next, q.next
    
            # If reach the end of one list
            if q.next:
                p.next = q.next
                r = p.next
    
            # Merge the remaining
            while r:
                if has_carry is True:
                    r.val += 1
                    has_carry = False
                if r.val >= 10:
                    has_carry = True
                    r.val = r.val % 10
                p = p.next
                r = p.next
    
            # If has_carry in the end
            if has_carry is True:
                tmp_node = ListNode(1)
                p.next = tmp_node
            return head