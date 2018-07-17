
# Leetcode: Decode Ways     :BLOG:Medium:

---

Decode Ways  

---

Similar Problems:  

-   [Review: Combinations and Permutations Problems](https://code.dennyzhang.com/review-combination)
-   [Review: Problems With Many Details](https://code.dennyzhang.com/review-manydetails)
-   Tag: [#manydetails](https://code.dennyzhang.com/tag/manydetails), [#combination](https://code.dennyzhang.com/tag/combination)

---

A message containing letters from A-Z is being encoded to numbers using the following mapping:  

    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26

Given an encoded message containing digits, determine the total number of ways to decode it.  

For example,  
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).  

The number of ways decoding "12" is 2.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/decode-ways)  

Credits To: [leetcode.com](https://leetcode.com/problems/decode-ways/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/decode-ways
    ## Basic Ideas: dynamic programming
    ##   
    ##   dp(n) = 
    ##        if s[n] == "0"
    ##            if s[n-1:n+1] is valid: s[n-2]
    ##            otherwise: 0
    ##        otherwise
    ##            if s[n-1:n+1] is valid: s[n-2] + s[n-1]
    ##            otherwise: s[n-1]
    ##
    ## Complexity: Time O(n), Space O(1)
    class Solution:
        def numDecodings(self, s):
    	"""
    	:type s: str
    	:rtype: int
    	"""
    	length = len(s)
    	if length == 0 or s[0] == '0': return 0
    	v1 = 1
    	if length == 1: return v1
    
    	# basic cases
    	if s[1] != '0':
    	    v2 = v1
    	else:
    	    v2 = 0
    	num = int(s[0:2])
    	if s[0] != '0' and num >= 1 and num <= 26:
    	    v2 += 1
    
    	if length == 2: return v2
    	# print(s, v1, v2)
    	# dp
    	for i in range(2, length):
    	    if s[i] == '0':
    		num = int(s[i-1:i+1])
    		if s[i-1] != '0' and num >= 1 and num <= 26:
    		    v3 = v1
    		else:
    		    v3 = 0
    	    else:
    		num = int(s[i-1:i+1])
    		if s[i-1] != '0' and num >= 1 and num <= 26:
    		    v3 = v1+v2
    		else:
    		    v3 = v2
    	    v2,v1 = v3,v2
    	return v2

