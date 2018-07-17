
# Leetcode: License Key Formatting     :BLOG:Basic:

---

License Key Formatting  

---

You are given a license key represented as a string S which consists only alphanumeric character and dashes. The string is separated into N+1 groups by N dashes.  

Given a number K, we would want to reformat the strings such that each group contains exactly K characters, except for the first group which could be shorter than K, but still must contain at least one character. Furthermore, there must be a dash inserted between two groups and all lowercase letters should be converted to uppercase.  

Given a non-empty string S and a number K, format the string according to the rules described above.  

    Example 1:
    Input: S = "5F3Z-2e-9-w", K = 4
    
    Output: "5F3Z-2E9W"
    
    Explanation: The string S has been split into two parts, each part has 4 characters.
    Note that the two extra dashes are not needed and can be removed.

    Example 2:
    Input: S = "2-5g-3-J", K = 2
    
    Output: "2-5G-3J"
    
    Explanation: The string S has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.

Note:  

1.  The length of string S will not exceed 12,000, and K is a positive integer.
2.  String S consists only of alphanumerical characters (a-z and/or A-Z and/or 0-9) and dashes(-).
3.  String S is non-empty.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/license-key-formatting)  

Credits To: [leetcode.com](https://leetcode.com/problems/license-key-formatting/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/license-key-formatting
    ## Basic Ideas: Get the length of non-dash string
    ##              Then we know how many dash we need
    ##              Move from right to left with two pointers
    ## Complexity: Time O(n), Space O(n) (If list instead of string, we can solve O(1) space)
    class Solution(object):
        def licenseKeyFormatting(self, S, K):
    	"""
    	:type S: str
    	:type K: int
    	:rtype: str
    	"""
    	length = len(S)
    	count_str = length - S.count('-')
    	count_group = count_str/K
    	if count_str % K != 0:
    	    count_group += 1
    
    	l = [None] * (count_str + count_group - 1)
    	# get result from the right to left
    	index, count = len(l)-1, K
    	for i in xrange(length-1, -1, -1):
    	    if index == -1:
    		break
    	    if count == 0:
    		l[index] = '-'
    		index, count = index-1, K
    
    	    ch = S[i]
    	    if ch != '-':
    		l[index] = ch.upper()
    		index, count = index-1, count-1
    	return ''.join(l)
    
    # s = Solution()
    # s.licenseKeyFormatting("--a-a-a-a--", 2)

