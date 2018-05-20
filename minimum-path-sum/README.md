# Leetcode: Minimum Path Sum     :BLOG:Basic:


---

Minimum Path Sum  

---

Similar Problems:  
-   [Review: Dynamic Programming Problems](https://code.dennyzhang.com/review-dynamicprogramming)
-   Tag: [#dynamicprogramming](https://code.dennyzhang.com/tag/dynamicprogramming)

---

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.  

Note: You can only move either down or right at any point in time.  

    Example 1:
    [[1,3,1],
     [1,5,1],
     [4,2,1]]
    Given the above grid map, return 7. Because the path 1->3->1->1->1 minimizes the sum.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/minimum-path-sum)  

Credits To: [leetcode.com](https://leetcode.com/problems/minimum-path-sum/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/minimum-path-sum
    ## Basic Ideas:
    ##           For point grid[i][j], think about the prevoius step of the minimize path
    ##           It should come from either grid[i-1][j] or grid[i][j-1].
    ##
    ##           So f(i, j) can be calculated from f(i-1, j) and f(i, j-1)
    ##           
    ##           Do we have to use the extra space to save the intermediate results?
    ##           No, we can reuse the original matrix
    ##
    ## Complexity: Time O(m*n), Space O(1)
    ##
    class Solution(object):
        def minPathSum(self, grid):
            """
            :type grid: List[List[int]]
            :rtype: int
            """
            m = len(grid)
            if m == 0: return 0
            n = len(grid[0])
            for i in xrange(m):
                for j in xrange(n):
                    # skip the first node
                    if i == 0 and j == 0:
                        continue
                    # first column
                    if j == 0:
                        grid[i][j] += grid[i-1][j]
                        continue
                    # first row
                    if i == 0:
                        grid[i][j] += grid[i][j-1]
                        continue
                    grid[i][j] = min(grid[i][j-1], grid[i-1][j]) + grid[i][j]
    
            return grid[-1][-1]