
# Leetcode: Combinations     :BLOG:Basic:

---

Given two integers n and k, return all possible combinations of k numbers out of 1 &#x2026; n.  

---

Similar Problems:  

-   [Review: Combinations and Permutations Problems](https://code.dennyzhang.com/review-combination), [Tag: #combination](https://code.dennyzhang.com/tag/combination)

---

Given two integers n and k, return all possible combinations of k numbers out of 1 &#x2026; n.  

For example,  
If n = 4 and k = 2, a solution is:  

[  
  [2,4],  
  [3,4],  
  [2,3],  
  [1,2],  
  [1,3],  
  [1,4],  
]  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/combinations)  

Credits To: [leetcode.com](https://leetcode.com/problems/combinations/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/combinations
    ## Basic Ideas:
    ##          Get an array of n element, either 0 or 1
    ## Complexity: Time (Permutation), Space ?
    class Solution(object):
        def combine(self, n, k):
    	"""
    	:type n: int
    	:type k: int
    	:rtype: List[List[int]]
    	"""
    	l = self.getCombine(n, k)
    	res = []
    	for combine in l:
    	    item = []
    	    for digit in xrange(n):
    		if combine[digit] == 1:
    		    item.append(digit + 1)
    	    if len(item) != 0:
    		res.append(item)
    	return res
    
        def getCombine(self, n, k):
    	if n == k:
    	    return [[1]*n]
    	if k > n or n == 0:
    	    return []
    	if k == 0:
    	    return [[0]*n]
    	res = []
    	res_0 = self.getCombine(n-1, k)
    	res_1 = self.getCombine(n-1, k-1)
    	if len(res_0) != 0:
    	    for item in res_0:
    		res.append([0] + item)
    
    	if len(res_1) != 0:
    	    for item in res_1:
    		res.append([1] + item)
    	return res
    
    # s = Solution()
    # print s.combine(4, 2)
    # print s.combine(1, 1)

