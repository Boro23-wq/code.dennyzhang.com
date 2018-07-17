
# Leetcode: Number Of Corner Rectangles     :BLOG:Medium:

---

Number Of Corner Rectangles  

---

Similar Problems:  

-   Tag: [#array](https://code.dennyzhang.com/tag/array)

---

Given a grid where each entry is only 0 or 1, find the number of corner rectangles.  

A corner rectangle is 4 distinct 1s on the grid that form an axis-aligned rectangle. Note that only the corners need to have the value 1. Also, all four 1s used must be distinct.  

Example 1:  

    
    Input: grid = 
    [[1, 0, 0, 1, 0],
     [0, 0, 1, 0, 1],
     [0, 0, 0, 1, 0],
     [1, 0, 1, 0, 1]]
    Output: 1
    Explanation: There is only one corner rectangle, with corners grid[1][2], grid[1][4], grid[3][2], grid[3][4].

Example 2:  

    Input: grid = 
    [[1, 1, 1],
     [1, 1, 1],
     [1, 1, 1]]
    Output: 9
    Explanation: There are four 2x2 rectangles, four 2x3 and 3x2 rectangles, and one 3x3 rectangle.

Example 3:  

    Input: grid = 
    [[1, 1, 1, 1]]
    Output: 0
    Explanation: Rectangles must have four distinct corners.

Note:  

1.  The number of rows and columns of grid will each be in the range [1, 200].
2.  Each grid[i][j] will be either 0 or 1.
3.  The number of 1s in the grid will be at most 6000.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/number-of-corner-rectangles)  

Credits To: [leetcode.com](https://leetcode.com/problems/number-of-corner-rectangles/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/number-of-corner-rectangles
    // Basic Ideas
    //
    // Keep the rows fixed, then check columns.
    // Or keep columns fixed, then check rows
    //
    // Complexity: Time O(n*n*m), Space O(1)
    func countCornerRectangles(grid [][]int) int {
        res := 0
        for i:=0; i<len(grid)-1; i++ {
    	for j:=i+1; j<len(grid); j++ {
    	    count:=0
    	    for k:=0; k<len(grid[0]); k++ {
    		if grid[i][k]==1 && grid[j][k]==1 {
    		    count++
    		}
    	    }
    	    res += (count*(count-1))/2
    	}
        }
        return res
    }

