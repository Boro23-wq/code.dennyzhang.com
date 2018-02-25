# Leetcode: Domino and Tromino Tiling     :BLOG:Medium:


---

Domino and Tromino Tiling  

---

Similar Problems:  
-   [Review: Dynamic Programming Problems](https://brain.dennyzhang.com/review-dynamicprogramming)

---

We have two types of tiles: a 2x1 domino shape, and an "L" tromino shape. These shapes may be rotated.  

    XX  <- domino
    
    XX  <- "L" tromino
    X

Given N, how many ways are there to tile a 2 x N board? Return your answer modulo 10^9 + 7.  

(In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.)  

Example:  

    Input: 3
    Output: 5
    Explanation: 
    The five different ways are listed below, different letters indicates different tiles:
    XYZ XXZ XYY XXY XYY
    XYZ YYZ XZZ XYY XXY

Note:  

N  will be in range [1, 1000].  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/domino-and-tromino-tiling)  

Credits To: [leetcode.com](https://leetcode.com/problems/domino-and-tromino-tiling/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/domino-and-tromino-tiling
    ## Basic Ideas: dynamic programming
    ##
    ## Complexity: Time O(n), Space O(1)
    class Solution:
        def numTilings(self, N):
            """
            :type N: int
            :rtype: int
            """
            if N==1: return 1
            if N==2: return 2
            if N==3: return 5
            mod_num = pow(10, 9)+7
            v3,v2,v1 = 5,2,1
            sum_v=4
    
            for i in range(4, N+1):
                v = (v3+v2+sum_v) % mod_num
                v3,v2,v1 = v,v3,v2
                sum_v=sum_v+v1*2
            return v3
    
    s = Solution()
    print(s.numTilings(4)) # 11
    print(s.numTilings(5)) # 24
    print(s.numTilings(6)) # 53