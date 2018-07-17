
# Leetcode: Palindrome Number     :BLOG:Basic:

---

Determine whether an integer is a palindrome. Do this without extra space.  

---

Similar Problems:  

-   [Review: Palindrome Problems](https://code.dennyzhang.com/review-palindrome)
-   Tag: [#palindrome](https://code.dennyzhang.com/tag/palindrome)

---

Determine whether an integer is a palindrome. Do this without extra space.  

Some hints:  

    Could negative integers be palindromes? (ie, -1)
    
    If you are thinking of converting the integer to string, note the restriction of using extra space.
    
    You could also try reversing an integer. However, if you have solved
    the problem "Reverse Integer", you know that the reversed integer
    might overflow. How would you handle such case?
    
    There is a more generic way of solving this problem.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/palindrome-number)  

Credits To: [leetcode.com](https://leetcode.com/problems/palindrome-number/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/palindrome-number
    ## Basic Ideas:  Generate a new integer Y from right digit to left digit
    ##               Then compare it with X
    ##         1234321: 1 -> 12 -> 13 -> 134 ...
    ## Complexity: Time O(1), Space O(1). The integer can be at most 32 digits
    class Solution(object):
        def isPalindrome(self, x):
    	"""
    	:type x: int
    	:rtype: bool
    	"""
    	if x < 0:
    	    return False
    	if x == 0:
    
    	    return True
    	val = x
    	y = 0
    	while val != 0:
    	    y = 10*y + (val%10)
    	    val = val / 10
    	return x == y

