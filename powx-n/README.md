# Leetcode: Pow(x, n)     :BLOG:Basic:


---

Implement pow(x, n).  

---

Similar Problems:  
-   [Super Pow](https://code.dennyzhang.com/super-pow)
-   [Review: Recursive Problems](https://code.dennyzhang.com/review-recursive), [Tag: #recursive](https://code.dennyzhang.com/tag/recursive)
-   Tag: [#math](https://code.dennyzhang.com/tag/math), [#recursive](https://code.dennyzhang.com/tag/recursive)

---

Implement pow(x, n).  

    Example 1:
    
    Input: 2.00000, 10
    Output: 1024.00000

    Example 2:
    
    Input: 2.10000, 3
    Output: 9.26100

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/powx-n)  

Credits To: [leetcode.com](https://leetcode.com/problems/powx-n/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/powx-n
    ## Basic Ideas: 
    ##        If n < 0, x^n == (1/x)^(-n)
    ##        If n%2 == 0, x^n == (x*x)^(n/2)
    ##        If n%2 == 1, x^n == x * (x*x)^((n-1)/2)
    ##
    ## Complexity: Time O(log(n)), Space O(1)
    class Solution(object):
        def myPow(self, x, n):
            """
            :type x: float
            :type n: int
            :rtype: float
            """
            if n == 0:
                return 1
            if n < 0:
                n = -n
                x = 1/x
            if n %2 == 0:
                return self.myPow(x*x, n/2)
            else:
                return x*self.myPow(x*x, (n-1)/2)