# Leetcode: Bomb Enemy     :BLOG:Medium:


---

Bomb Enemy  

---

Similar Problems:  
-   [Lonely Pixel I](https://brain.dennyzhang.com/lonely-pixel-i)
-   [Review: Dynamic Programming Problems](https://brain.dennyzhang.com/review-dynamicprogramming), [Tag: #dynamicprogramming](https://brain.dennyzhang.com/tag/dynamicprogramming)
-   [Review: Game Problems](https://brain.dennyzhang.com/review-game), [Tag: #game](https://brain.dennyzhang.com/tag/game)

---

Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.  
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.  
Note that you can only put the bomb at an empty cell.  

Example:  

    For the given grid
    
    0 E 0 0
    E 0 W E
    0 E 0 0
    
    return 3. (Placing a bomb at (1,1) kills 3 enemies)

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/bomb-enemy)  

Credits To: [leetcode.com](https://leetcode.com/problems/bomb-enemy/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/bomb-enemy
    ## Basic Ideas: dynamic programming
    ##
    ## dp[i][j] = [x1, y1, x2, y2]
    ##  x1: from top to current row
    ##      How many enemies boom[i][j] can kill
    ##  y1: from left to current column
    ##  x2: from bottom to current row
    ##  y2: from right to current column
    ##
    ## Assumption: if we place a boom in 'W', we will kill no enemies
    ##
    ## Complexity: Time O(m*n), Space O(m*n)
    class Solution:
        def maxKilledEnemies(self, grid):
            """
            :type grid: List[List[str]]
            :rtype: int
            """
            row_count = len(grid)
            if row_count == 0: return 0
            col_count = len(grid[0])
    
            dp = [[[0, 0, 0, 0] for j in range(col_count)] for i in range(row_count)]
    
            # caculate: x1, y1. 
            for i in range(row_count):
                for j in range(col_count):
                    ch = grid[i][j]
                    if ch == 'W':
                        dp[i][j] = [0, 0, 0, 0]
                    else:
                        k = 1 if ch == 'E' else 0
                        dp[i][j] = [dp[i-1][j][0]+k if i>0 else k, \
                                    dp[i][j-1][1]+k if j>0 else k, \
                                    k, k]
    
            max_count = 0
            # caculate: x2, y2, and get the result
            for i in range(row_count-1, -1, -1):
                for j in range(col_count-1, -1, -1):
                    ch = grid[i][j]
                    if ch == 'W': continue
                    k = 1 if ch == 'E' else 0
                    dp[i][j][2] = dp[i+1][j][2]+k if i<row_count-1 else k
                    dp[i][j][3] = dp[i][j+1][3]+k if j<col_count-1 else k
                    # get result
                    if grid[i][j] == '0':
                        max_count = max(max_count, sum(dp[i][j]))
    
            return max_count