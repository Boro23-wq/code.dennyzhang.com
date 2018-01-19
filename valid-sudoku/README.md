# Leetcode: Valid Sudoku     :BLOG:Basic:


---

Identity number which appears exactly once.  

---

Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.  

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.  

A partially filled sudoku which is valid.  

Note:  
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.  

Blog link: <http://brain.dennyzhang.com/valid-sudoku>  

Github: challenges-leetcode-interesting  

Credits To: leetcode.com  

Leave me comments, if you know how to solve.  

    ## Basic Ideas: Check each row, each colum and each section
    ##              When we check, we use an array of 10
    ##
    ## Complexity: Time O(1), Space O(1)
    class Solution(object):
        def isValidSudoku(self, board):
            """
            :type board: List[List[str]]
            :rtype: bool
            """
            # check each row
            for i in xrange(9):
                array_check = [False] * 9
                for j in xrange(9):
                    ch = board[i][j]
                    if ch == '.':
                        continue
                    index = int(ch) - 1
                    if array_check[index] is True:
                        return False
                    else:
                        array_check[index] = True
    
            # check each column
            for j in xrange(9):
                array_check = [False] * 9
                for i in xrange(9):
                    ch = board[i][j]
                    if ch == '.':
                        continue
                    index = int(ch) - 1
                    if array_check[index] is True:
                        return False
                    else:
                        array_check[index] = True
    
            # check each section
            start_node_list = []
            for i in [0, 3, 6]:
                for j in [0, 3, 6]:
                    start_node_list.append((i, j))
            for (start_i, start_j) in start_node_list:
                array_check = [False] * 9
                for i in xrange(3):
                    for j in xrange(3):
                        ch = board[start_i+i][start_j+j]
                        # print("i:%d, j:%d, ch:%s" % (start_i+i, start_j+j, ch))
                        # print array_check
                        if ch == '.':
                            continue
                        index = int(ch) - 1
                        if array_check[index] is True:
                            return False
                        else:
                            array_check[index] = True    
            return True