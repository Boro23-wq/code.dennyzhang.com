# Leetcode: Hamming Distance     :BLOG:Medium:


---

Hamming Distance  

---

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.  

Given two integers x and y, calculate the Hamming distance.  

Note:  
0 <= x, y < 231.  

    Example:
    
    Input: x = 1, y = 4
    
    Output: 2
    
    Explanation:
    1   (0 0 0 1)
    4   (0 1 0 0)
           .   .
    
    The above arrows point to positions where the corresponding bits are different.

Blog link: <http://brain.dennyzhang.com/hamming-distance>  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/hamming-distance)  

Credits To: [leetcode.com](https://leetcode.com/problems/hamming-distance/description)  

Leave me comments, if you know how to solve.  

    ## Basic Ideas: x xor y
    ##              Any bit of 1 for the result indicates a difference
    ## Complexity
    class Solution(object):
        def hammingDistance(self, x, y):
            """
            :type x: int
            :type y: int
            :rtype: int
            """
            num = x ^ y
            res = 0
            while num != 0:
                if num % 2 == 1:
                    res += 1
                num = num >> 1
            return res