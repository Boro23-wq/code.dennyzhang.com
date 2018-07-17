
# Leetcode: Verify Preorder Sequence in Binary Search Tree     :BLOG:Medium:

---

Verify Preorder Sequence in Binary Search Tree  

---

Similar Problems:  

-   [Verify Preorder Serialization of a Binary Tree](https://code.dennyzhang.com/verify-preorder-serialization-of-a-binary-tree)
-   [Review: Binary Tree Problems](https://code.dennyzhang.com/review-binarytree), [Tag: #binarytree](https://code.dennyzhang.com/tag/binarytree)

---

Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.  

You may assume each number in the sequence is unique.  

Follow up:  
Could you do it using only constant space complexity?  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/verify-preorder-sequence-in-binary-search-tree)  

Credits To: [leetcode.com](https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/verify-preorder-sequence-in-binary-search-tree
    import sys
    class Solution(object):
        def verifyPreorder(self, preorder):
    	"""
    	:type preorder: List[int]
    	:rtype: bool
    	"""
    	return self.myVerifyPreorder(preorder, -sys.maxsize-1)
    
        def myVerifyPreorder(self, preorder, min_val):
    	# print(preorder)
    	length = len(preorder)
    	if length == 0: return True
    
    	index = sys.maxsize
    	for i in range(length):
    	    if preorder[i] < min_val: return False
    	    if i != 0 and preorder[i] > preorder[0]:
    		index = i
    		break
    
    	# left sub-tree
    	if self.myVerifyPreorder(preorder[1:index], min_val) is False:
    	    return False
    
    	# if index == sys.maxsize, right sub-tree is empty
    	# right sub-tree
    	if self.myVerifyPreorder(preorder[index:], preorder[0]) is False:
    	    return False
    
    	return True
    
    # s = Solution()
    # print(s.verifyPreorder([10,7,4,8,6,40,23]))

