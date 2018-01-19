# Leetcode: Number of 1 Bits     :BLOG:Basic:


---

Number of 1 Bits  

---

Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).  

For example, the 32-bit integer '11' has binary representation 00000000000000000000000000001011, so the function should return 3.  

Blog link: <http://brain.dennyzhang.com/number-of-1-bits>  

Github: challenges-leetcode-interesting  

Credits To: leetcode.com  

Leave me comments, if you know how to solve.  

    class Solution(object):
        def hammingWeight(self, n):
            """
            :type n: int
            :rtype: int
            """
            count = 0
            while n != 0:
                if (n % 2) == 1:
                    count = count + 1
                n = n /2
            return count