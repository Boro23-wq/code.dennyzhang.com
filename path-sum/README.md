# Leetcode: Path Sum     :BLOG:Basic:


---

Path Sum  

---

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.  

    For example:
    Given the below binary tree and sum = 22,
                  5
                 / \
                4   8
               /   / \
              11  13  4
             /  \      \
            7    2      1
    return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/path-sum)  

Credits To: [leetcode.com](https://leetcode.com/problems/path-sum/description/)  

Leave me comments, if you know how to solve.  

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def hasPathSum(self, root, sum):
            if root is None:
                return False
            queue = []
            queue.append((root, 0))
            while len(queue) != 0:
                (element, current_sum) = queue[0]
                del queue[0]
                if element.left is None and element.right is None:
                    if element.val + current_sum == sum:
                        return True
                if element.left:
                    queue.append((element.left, current_sum + element.val))
                if element.right:
                    queue.append((element.right, current_sum + element.val))
            return False
    
        def hasPathSum_v1(self, root, sum):
            """
            :type root: TreeNode
            :type sum: int
            :rtype: bool
            """
            ## Idea: DFS recursive, BFS
            ## Complexity: Time O(n), Space O(log(k))
            return self._hasPathSum(root, sum, 0)
    
        def _hasPathSum(self, root, sum, current_sum):
            if root is None:
                return False
            if root.left is None and root.right is None:
                return root.val + current_sum == sum
    
            if root.left:
                if self._hasPathSum(root.left, sum, current_sum + root.val):
                    return True
    
            if root.right:
                if self._hasPathSum(root.right, sum, current_sum + root.val):
                    return True
    
            return False