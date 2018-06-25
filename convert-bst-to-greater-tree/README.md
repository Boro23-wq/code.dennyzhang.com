
# Leetcode: Convert BST to Greater Tree     :BLOG:Basic:

---

Tree traversal: right, middle, left  

---

Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.  

    Example:
    
    Input: The root of a Binary Search Tree like this:
                  5
                /   \
               2     13
    
    Output: The root of a Greater Tree like this:
                 18
                /   \
              20     13

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/convert-bst-to-greater-tree)  

Credits To: [leetcode.com](https://leetcode.com/problems/convert-bst-to-greater-tree/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/convert-bst-to-greater-tree
    ## Basic Ideas: Tree traversal: right, middle, left
    ##              Visit nodes in a descending way
    ##           TODO: how to do it in a recusive way?
    ## Complexity:
    ## Sample Data:
    ##           10
    ##         /   \
    ##        5     13
    ##       / \    /
    ##      2   7  11
    ##
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def convertBST(self, root):
    	"""
    	:type root: TreeNode
    	:rtype: TreeNode
    	"""
    	stack = []
    	p = root
    	while p:
    	    stack.append(p)
    	    p = p.right
    
    	previous_node = None
    	while len(stack) != 0:
    	    top_element = stack.pop()
    	    if previous_node:
    		top_element.val += previous_node.val
    	    previous_node = top_element
    	    if top_element.left:
    		p = top_element.left
    		while p:
    		    stack.append(p)
    		    p = p.right
    	return root            

