
# Leetcode: Sliding Puzzle     :BLOG:Basic:

---

Sliding Puzzle  

---

Similar Problems:  

-   [LintCode: Sliding Puzzle III](https://code.dennyzhang.com/sliding-puzzle-iii)
-   [Review: Game Problems](https://code.dennyzhang.com/review-game)
-   Tag: [#graph](https://code.dennyzhang.com/tag/graph), [#game](https://code.dennyzhang.com/tag/game)

---

On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.  

A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.  

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].  

Given a puzzle board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.  

Examples:  

    Input: board = [[1,2,3],[4,0,5]]
    Output: 1
    Explanation: Swap the 0 and the 5 in one move.

    Input: board = [[1,2,3],[5,4,0]]
    Output: -1
    Explanation: No number of moves will make the board solved.

    Input: board = [[4,1,2],[5,0,3]]
    Output: 5
    Explanation: 5 is the smallest number of moves that solves the board.
    An example path:
    After move 0: [[4,1,2],[5,0,3]]
    After move 1: [[4,1,2],[0,5,3]]
    After move 2: [[0,1,2],[4,5,3]]
    After move 3: [[1,0,2],[4,5,3]]
    After move 4: [[1,2,0],[4,5,3]]
    After move 5: [[1,2,3],[4,5,0]]
    Input: board = [[3,2,4],[1,5,0]]
    Output: 14

Note:  

-   board will be a 2 x 3 array as described above.
-   board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/sliding-puzzle)  

Credits To: [leetcode.com](https://leetcode.com/problems/sliding-puzzle/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/sliding-puzzle
    ## Basic Ideas: BFS: find the mininum path from point1 to point2
    ##
    ## Complexity:
    class Solution(object):
        def slidingPuzzle(self, board):
    	"""
    	:type board: List[List[int]]
    	:rtype: int
    	"""
    	target = '123450'
    	queue, visited = [], set()
    	queue.append(self.toString(board))
    
    	level = 0
    	while len(queue) != 0:
    	    for i in range(len(queue)):
    		state = queue[0]
    		if state == target: return level
    		del queue[0]
    		visited.add(state)
    		# move to next
    		self.addNeighbors(state, visited, queue)
    		# print queue
    	    level += 1
    	return -1
    
        def toString(self, board):
    	res = ''
    	for i in range(2):
    	    for j in range(3):
    		res = res + str(board[i][j])
    	return res
    
        def addNeighbors(self, state, visited, queue):
    	# change back state to board
    	matrix = [[None for j in range(3)] for i in range(2)]
    	index = 0
    	i0, j0 = None, None
    	for i in range(2):
    	    for j in range(3):
    		matrix[i][j] = state[index]
    		index += 1
    		if matrix[i][j] == '0':
    		    i0, j0 = i, j
    	# get next: 
    	for (ik, jk) in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
    	    i2, j2 = i0+ik, j0+jk
    	    if i2<0 or i2 >= 2 or j2<0 or j2>=3: continue
    	    matrix[i0][j0], matrix[i2][j2] = matrix[i2][j2], matrix[i0][j0]
    	    newState = self.toString(matrix)
    	    if newState not in visited:
    		queue.append(newState)
    	    # change back
    	    matrix[i0][j0], matrix[i2][j2] = matrix[i2][j2], matrix[i0][j0]

