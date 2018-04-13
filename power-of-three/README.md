# Leetcode: Power of Three     :BLOG:Amusing:


---

Given an integer, write a function to determine if it is a power of three.  

---

Similar Problems:  
-   [Review: Math Problems,](https://code.dennyzhang.com/review-math) Tag: [math](https://code.dennyzhang.com/tag/math)

---

Given an integer, write a function to determine if it is a power of three.  

Follow up:  
Could you do it without using any loop / recursion?  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/power-of-three)  

Credits To: [leetcode.com](https://leetcode.com/problems/power-of-three/description/)  

Leave me comments, if you have better ways to solve.  

    class Solution(object):
    ## Blog link: https://code.dennyzhang.com/power-of-three
    ## Basic Ideas: power of any prime number
    ##              3 is a prime
    ##              If 3 % k == 0 and k is a prime, then k is 3.
    ##              Thus 3^19 % n === 0 means n is power of 3
    class Solution(object):
        def isPowerOfThree(self, n):
            """
            :type n: int
            :rtype: bool
            """
            if n <= 0:
                return False
            larget_power3 = pow(3, 19)
            return larget_power3 % n == 0