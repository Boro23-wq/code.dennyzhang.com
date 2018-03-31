# Leetcode: Gray Code     :BLOG:Medium:


---

Gray Code  

---

Similar Problems:  
-   [Lexicographical Numbers](https://brain.dennyzhang.com/lexicographical-numbers)
-   [Review: Dynamic Programming Problems](https://brain.dennyzhang.com/review-dynamicprogramming)
-   Tag: [#dynamicprogramming](https://brain.dennyzhang.com/tag/dynamicprogramming)

---

The gray code is a binary numeral system where two successive values differ in only one bit.  

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.  

    For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
    
    00 - 0
    01 - 1
    11 - 3
    10 - 2

Note:  
For a given n, a gray code sequence is not uniquely defined.  

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.  

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/gray-code)  

Credits To: [leetcode.com](https://leetcode.com/problems/gray-code/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/gray-code
    class Solution:
        def grayCode(self, n):
            """
            :type n: int
            :rtype: List[int]
            """
            res = [0]
            for i in range(n):
                v = pow(2, i)
                for j in range(len(res)-1, -1, -1):
                    res.append(res[j]+v)
            return res
    
        ## Basic Ideas: dynamic programming
        ##  get f(n) from f(n-1)
        ##      copy the original
        ##      add pow(2, n-1) to each item from right to left
        ##
        ##   from f(2) to f(3)
        ##      00 01 11 10
        ##      00 01 11 10 110 111 101 100
        ## Complexity:
        def grayCode_v1(self, n):
            """
            :type n: int
            :rtype: List[int]
            """
            if n <= 0: return [0]
            if n == 1: return [0, 1]
            import copy
            l = [0, 1]
            for i in range(2, n+1):
                l2 = copy.deepcopy(l)
                v = pow(2, i-1)
                for k in range(len(l)-1, -1, -1):
                    l2.append(v+l[k])
                l = l2
            return l
    
    # s = Solution()
    # print(s.grayCode(2))
    # print(s.grayCode(3))