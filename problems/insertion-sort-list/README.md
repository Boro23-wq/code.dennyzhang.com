
# Leetcode: Insertion Sort List     :BLOG:Basic:

---

Sort a linked list  

---

Sort a linked list using insertion sort.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/insertion-sort-list)  

Credits To: [leetcode.com](https://leetcode.com/problems/insertion-sort-list/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/insertion-sort-list
    ## Basic Ideas: 
    ##       Add a dummy head node, since the head node might be changed
    ##       Pointer p: the tail of sorted list
    ##       Pointer q: the next node to be sorted
    ## Complexity
    ## Sample Data:
    ##     2 -> 3 -> 5 -> 1
    ##          p
    ##               q
    ##     r
    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def insertionSortList(self, head):
    	"""
    	:type head: ListNode
    	:rtype: ListNode
    	"""
    	dummy_node = ListNode(None)
    	dummy_node.next = head
    	p = dummy_node.next
    	# quit if no node to be sorted
    	while p and p.next:
    	    q = p.next
    	    r = dummy_node
    	    # quit if we have compared q with all sorted elements
    	    while r != p:
    		if r.next.val > q.val:
    		    break
    		r = r.next
    	    if r != p:
    		# move q to the next of r
    		p.next = q.next
    		q.next = r.next
    		r.next = q
    	    else:
    		p = p.next
    	return dummy_node.next
    
    # s = Solution()
    # p1 = ListNode(3)
    # p2 = ListNode(4)
    # p3 = ListNode(1)
    
    # p1 = ListNode(3)
    # p2 = ListNode(2)
    # p3 = ListNode(4)
    # 
    # p1 = ListNode(3)
    # p2 = ListNode(2)
    # p3 = ListNode(1)
    
    # p1.next = p2
    # p2.next = p3
    # p3.next = None
    # 
    # new_head = s.insertionSortList(p1)
    # print new_head.val
    # print new_head.next.val
    # print new_head.next.next.val

