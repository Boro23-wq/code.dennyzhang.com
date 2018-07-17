
# Leetcode: Minimum Absolute Difference in BST     :BLOG:Basic:

---

Minimum Absolute Difference in BST  

---

Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.  

    Example:
    
    Input:
    
       1
        \
         3
        /
       2
    
    Output:
    1
    
    Explanation:
    The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
    Note: There are at least two nodes in this BST.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/minimum-absolute-difference-in-bst)  

Credits To: [leetcode.com](https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/minimum-absolute-difference-in-bst
    ## Basic Ideas: In-order trasveral
    ##
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        ##
        ## Complexity: Time O(n), Space O(h) # h: height
        def getMinimumDifference(self, root):
    	"""
    	:type root: TreeNode
    	:rtype: int
    	"""
    	stack = []
    	# initialize the stack
    	node = root
    	while node:
    	    stack.append(node)
    	    node = node.left
    
    	res = sys.maxsize
    	prev, node = None, None
    	# visit nodes
    	while len(stack) != 0:
    	    node = stack[-1]
    	    del stack[-1]
    	    if prev:
    		res = min(res, abs(prev.val-node.val))
    	    prev = node
    	    if node.right:
    		node = node.right
    		while node:
    		    stack.append(node)
    		    node = node.left
    	return res
    
        ## Blog link: https://code.dennyzhang.com/minimum-absolute-difference-in-bst
    ## Basic Ideas:
        ##         For the target pair, it won't be in two sub-trees.
        ##         So it will be parent-child.
        ##
        ##         For each node, check the last node of the left sub-tree.
        ##                        Then check the first node of right sub-tree
        ##
        ## Complexity: Time O(log(n)*n), Space O(d). # d: width
        def getMinimumDifference_v1(self, root):
    	"""
    	:type root: TreeNode
    	:rtype: int
    	"""
    	res = sys.maxsize
    	queue = []
    	queue.append(root)
    	while len(queue) != 0:
    	    for i in xrange(len(queue)):
    		node = queue[0]
    		del queue[0]
    		if node.left:
    		    p = node.left
    		    while p.right: p = p.right
    		    res = min(abs(node.val - p.val), res)
    		    queue.append(node.left)
    		if node.right:
    		    p = node.right
    		    while p.left: p = p.left
    		    res = min(abs(node.val - p.val), res)
    		    queue.append(node.right)
    	return res

