
# Leetcode: Populating Next Right Pointers in Each Node II     :BLOG:Hard:

---

Populating Next Right Pointers in Each Node II  

---

Similar Problems:  

-   [Review: Problems With Many Details](https://code.dennyzhang.com/review-manydetails)
-   Tag: [#manydetails](https://code.dennyzhang.com/tag/manydetails)

---

Follow up for problem "Populating Next Right Pointers in Each Node".  

What if the given tree could be any binary tree? Would your previous solution still work?  

Note:  

You may only use constant extra space.  

    For example,
    Given the following binary tree,
             1
           /  \
          2    3
         / \    \
        4   5    7
    After calling your function, the tree should look like:
             1 -> NULL
           /  \
          2 -> 3 -> NULL
         / \    \
        4-> 5 -> 7 -> NULL

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/populating-next-right-pointers-in-each-node-ii)  

Credits To: [leetcode.com](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/populating-next-right-pointers-in-each-node-ii
    ## Basic Ideas: Process nodes: from top to down, left to right
    ##              How to process:
    ##                 p.left.next = p.right
    ##                 p.right = p.next.left
    ##              How to move to next node?
    ##                 p.next
    ##                 first: first node of next layer
    ## Complexity: Time O(n), Space O(1)
    # Definition for binary tree with next pointer.
    # class TreeLinkNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    #         self.next = None
    
    class Solution:
        # @param root, a tree link node
        # @return nothing
        def connect(self, root):
    	if root is None:
    	    return
    	p = root
    	first = p.left if root.left else root.right
    	while p:
    	    # process p
    	    if p.left and p.right:
    		p.left.next = p.right
    		if p.next:
    		    p.right.next = self.getNextRight(p)
    	    elif p.left:
    		# only left sub-tree
    		if p.next:
    		    p.left.next = self.getNextRight(p)
    	    elif p.right:
    		# only right sub-tree
    		if p.next:
    		    p.right.next = self.getNextRight(p)
    
    	    # move to next node
    	    if p.next:
    		p = p.next
    	    else:
    		p = first
    		first = self.getNextFirst(first)
    
        def getNextFirst(self, p):
    	while p and p.left is None and p.right is None:
    	    p = p.next
    	if p is None:
    	    return None
    	else:
    	    return p.left if p.left else p.right
    
        def getNextRight(self, p):  
    	q = p.next
    	while q:
    	    # process q
    	    if q.left or q.right:
    		return q.left if q.left else q.right
    	    q = q.next
    	return None

