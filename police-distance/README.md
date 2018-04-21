# LintCode: Police Distance     :BLOG:Medium:


---

Police Distance  

---

Similar Problems:  
-   Tag: [#bfs](https://code.dennyzhang.com/tag/bfs)

---

Given a matrix size of n x m, element 1 represents policeman, -1 represents wall and 0 represents empty.  
Now please output a matrix size of n x m, output the minimum distance between each empty space and the nearest policeman  

 Notice  
Given a matrix size of n x m, n <= 200,m <= 200.  
We guarantee that each empty space can be reached by one policeman at least.  
Have you met this question in a real interview?  
Example  

    Given mat =
    
    [
        [0, -1, 0],
        [0, 1, 1],
        [0, 0, 0]
    ]
    return [[2,-1,1],[1,0,0],[2,1,1]].

    The distance between the policeman and himself is 0, the shortest distance between the two policemen to other empty space is as shown above
    Given mat =
    
    [
        [0, -1, -1],
        [0, -1, 1],
        [0, 0, 0]
    ]
    
    return `[[5,-1,-1],[4,-1,0],[3,2,1]]`
    The shortest distance between the policemen to other 5 empty space is as shown above.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/police-distance)  

Credits To: [lintcode.com](http://www.lintcode.com/en/problem/police-distance/)  
Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/police-distance
    class Solution:
        """
        @param matrix : the martix
        @return: the distance of grid to the police
        """
        def policeDistance(self, matrix):
            ## Basic Ideas: BFS
            ## Complexity: Time O(n*m), Space O(n*m)
            row_count = len(matrix)
            if row_count == 0: return None
            col_count = len(matrix[0])
            res = [[0 for j in range(col_count)] for i in range(row_count)]
    
            import collections
            queue = collections.deque()
            seen = set([])
    
            for i in range(row_count):
                for j in range(col_count):
                    if matrix[i][j] == -1:
                        res[i][j] = -1
                        seen.add((i, j))
                    if matrix[i][j] == 1:
                        queue.append((i, j))
                        seen.add((i, j))
            level = 0
            while len(queue) != 0:
                level += 1
                for k in range(len(queue)):
                    (i, j) = queue.popleft()
                    for (offset_i, offset_j) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        i2, j2 = i+offset_i, j+offset_j
                        if i2<0 or i2>=row_count or j2<0 or j2>=col_count:
                            continue
                        if matrix[i2][j2] == 0 and (i2, j2) not in seen:
                            res[i2][j2] = level
                            queue.append((i2, j2))
                            seen.add((i2, j2))
            return res