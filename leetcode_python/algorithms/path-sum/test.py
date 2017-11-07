#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Tags:
## Description:
##     https://leetcode.com/problems/path-sum/description/
##    ,-----------
##    | Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
##    | 
##    | For example:
##    | Given the below binary tree and sum = 22,
##    |               5
##    |              / \
##    |             4   8
##    |            /   / \
##    |           11  13  4
##    |          /  \      \
##    |         7    2      1
##    | return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
##    `-----------
##
##
## Basic Idea:
## Complexity:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:16>
##-------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
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
        