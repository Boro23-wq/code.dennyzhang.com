# Leetcode: Same Tree     :BLOG:Medium:


---

Given two binary trees, write a function to check if they are the same or not.  

---

Given two binary trees, write a function to check if they are the same or not.  

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.  

    Example 1:
    Input:     1         1
              / \       / \
             2   3     2   3
    
            [1,2,3],   [1,2,3]
    
    Output: true

    Example 2:
    
    Input:     1         1
              /           \
             2             2
    
            [1,2],     [1,null,2]
    
    Output: false

    Example 3:
    
    Input:     1         1
              / \       / \
             2   1     1   2
    
            [1,2,1],   [1,1,2]
    
    Output: false

Blog link: <http://brain.dennyzhang.com/same-tree>  

Github: challenges-leetcode-interesting  

Credits To: leetcode.com  

Leave me comments, if you know how to solve.  

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def isSameTree(self, p, q):
            """
            :type p: TreeNode
            :type q: TreeNode
            :rtype: bool
            """
            if (p is None) and (q is None):
                return True
            else:
                if (p is None) or (q is None):
                    return False
                else:
                    if p.val != q.val:
                        return False
                    else:
                        if self.isSameTree(p.left, q.left) is False:
                            return False
                        if self.isSameTree(p.right, q.right) is False:
                            return False
                        return True