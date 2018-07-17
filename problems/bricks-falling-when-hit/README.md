
# Leetcode: Bricks Falling When Hit     :BLOG:Hard:

---

Bricks Falling When Hit  

---

Similar Problems:  

-   Tag: [#graph](https://code.dennyzhang.com/tag/graph), [#game](https://code.dennyzhang.com/tag/game), [#inspiring](https://code.dennyzhang.com/tag/inspiring)

---

We have a grid of 1s and 0s; the 1s in a cell represent bricks.  A brick will not drop if and only if it is directly connected to the top of the grid, or at least one of its (4-way) adjacent bricks will not drop.  

We will do some erasures sequentially. Each time we want to do the erasure at the location (i, j), the brick (if it exists) on that location will disappear, and then some other bricks may drop because of that erasure.  

Return an array representing the number of bricks that will drop after each erasure in sequence.  

Example 1:  

    Input: 
    grid = [[1,0,0,0],[1,1,1,0]]
    hits = [[1,0]]
    Output: [2]
    Explanation: 
    If we erase the brick at (1, 0), the brick at (1, 1) and (1, 2) will drop. So we should return 2.

Example 2:  

    Input: 
    grid = [[1,0,0,0],[1,1,0,0]]
    hits = [[1,1],[1,0]]
    Output: [0,0]
    Explanation: 
    When we erase the brick at (1, 0), the brick at (1, 1) has already disappeared due to the last move. So each erasure will cause no bricks dropping.  Note that the erased brick (1, 0) will not be counted as a dropped brick.

Note:  

-   The number of rows and columns in the grid will be in the range [1, 200].
-   The number of erasures will not exceed the area of the grid.
-   It is guaranteed that each erasure will be different from any other erasure, and located inside the grid.
-   An erasure may refer to a location with no brick - if it does, no bricks drop.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/bricks-falling-when-hit)  

Credits To: [leetcode.com](https://leetcode.com/problems/bricks-falling-when-hit/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/bricks-falling-when-hit
    // Basic Ideas: DFS
    // Complexity: Time O(n*m*len(hits)), Space O(n*m)
    var visits [][]int
    func dfs(i int, j int, grid[][]int, row_count int, col_count int) bool {
        if i<0 || i>=row_count || j<0 || j>=col_count { return false }
        if grid[i][j] != 1 { return false }
        if i == 0 { return true }
    
        grid[i][j] = 2
        visits = append(visits, []int{i, j})
        if dfs(i+1, j, grid, row_count, col_count) { return true }
        if dfs(i-1, j, grid, row_count, col_count) { return true }
        if dfs(i, j+1, grid, row_count, col_count) { return true }
        if dfs(i, j-1, grid, row_count, col_count) { return true }
        // fmt.Println("dfs, i: ", i, " j:", j, " visits: ", visits)
        return false
    }
    
    func hitBricks(grid [][]int, hits [][]int) []int {
        row_count, col_count := len(grid), len(grid[0])
        res := []int{}
        for _, position := range hits {
    	x, y := position[0], position[1]
    	count := 0
    	if grid[x][y] == 1 {
    	    grid[x][y] = 0
    	    // explore in 4 directions
    	    for _, offset := range [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}} {
    		x2, y2 := x+offset[0], y+offset[1]
    		visits = [][]int{}
    		is_ok := dfs(x2, y2, grid, row_count, col_count)
    		// fmt.Println("x2:", x2, " y2:", y2, " is_ok:", is_ok, " visits:", visits)
    		if is_ok == true {
    		    // undo
    		    for k, _ := range visits {
    			grid[visits[k][0]][visits[k][1]] = 1
    		    }
    		} else {
    		    count += len(visits)
    		    for k, _ := range visits {
    			grid[visits[k][0]][visits[k][1]] = 0
    		    }
    		}
    	    }
    	}
    	res = append(res, count)
        }
        return res
    }

