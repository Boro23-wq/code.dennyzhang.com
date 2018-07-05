# Leetcode: The Maze     :BLOG:Medium:


---

The Maze  

---

Similar Problems:  
-   Tag: [#bfs](https://code.dennyzhang.com/tag/bfs), [#game](https://code.dennyzhang.com/tag/game), [#inspiring](https://code.dennyzhang.com/tag/inspiring), [#manydetails](https://code.dennyzhang.com/tag/manydetails)

---

There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.  

Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.  

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.  

Example 1  

    Input 1: a maze represented by a 2D array
    
    0 0 1 0 0
    0 0 0 0 0
    0 0 0 1 0
    1 1 0 1 1
    0 0 0 0 0
    
    Input 2: start coordinate (rowStart, colStart) = (0, 4)
    Input 3: destination coordinate (rowDest, colDest) = (4, 4)
    
    Output: true
    Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right

![img](//raw.githubusercontent.com/DennyZhang/images/master/code/maze_1_1.png)  

Example 2  

    Input 1: a maze represented by a 2D array
    
    0 0 1 0 0
    0 0 0 0 0
    0 0 0 1 0
    1 1 0 1 1
    0 0 0 0 0
    
    Input 2: start coordinate (rowStart, colStart) = (0, 4)
    Input 3: destination coordinate (rowDest, colDest) = (3, 2)
    
    Output: false
    Explanation: There is no way for the ball to stop at the destination.

![img](//raw.githubusercontent.com/DennyZhang/images/master/code/maze_1_2.png)  

Note:  
1.  There is only one ball and one destination in the maze.
2.  Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
3.  The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
4.  The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/the-maze)  

Credits To: [leetcode.com](https://leetcode.com/problems/the-maze/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/the-maze
    // Basic Idea: BFS
    //
    // Items to be explored would be positions which are near to walls
    // Once visisted, mark it to 2
    //
    // Complexity: Time O(n), Space O(1)
    type Node struct {
        x, y int
    }
    
    func hasPath(maze [][]int, start []int, destination []int) bool {
        queue := []Node{Node{start[0], start[1]}}
        x2, y2 := 0, 0
        for len(queue) != 0 {
            items := []Node{}
            for _, node := range queue {
                maze[node.x][node.y] = 2 // mark as visited
                for _, offset := range [][]int {{0, 1}, {0, -1}, {1, 0}, {-1, 0}} {
                        // move the wall in current direction
                        x2, y2 = node.x+offset[0], node.y+offset[1]
                        // We can't use maze[x2][y2] == 0. We can only stop by walls. Not visited nodes
                        for x2>=0 && x2<len(maze) && y2>=0 && y2<len(maze[0]) && maze[x2][y2] != 1 {
                            x2, y2 = x2+offset[0], y2+offset[1]
                        }
                        // move back
                        x2, y2 = x2-offset[0], y2-offset[1]
                        if x2==node.x && y2==node.y { continue }
                        if maze[x2][y2] == 0 {
                            if x2==destination[0] && y2==destination[1] { return true }
                            items = append(items, Node{x2, y2})
                        }
                    }
            }
            queue = items
        }
        return false
    }