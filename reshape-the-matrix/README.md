# Leetcode: Reshape the Matrix     :BLOG:Basic:


---

Reshape the Matrix  

---

Similar Problems:  
-   Tag: [matrixtraverse](https://brain.dennyzhang.com/tag/matrixtraverse)

---

In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.  

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.  

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.  

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.  

    Example 1:
    Input: 
    nums = 
    [[1,2],
     [3,4]]
    r = 1, c = 4
    Output: 
    [[1,2,3,4]]
    Explanation:
    The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.

    Example 2:
    Input: 
    nums = 
    [[1,2],
     [3,4]]
    r = 2, c = 4
    Output: 
    [[1,2],
     [3,4]]
    Explanation:
    There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.

Note:  
1.  The height and width of the given matrix is in range [1, 100].
2.  The given r and c are all positive.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/reshape-the-matrix)  

Credits To: [leetcode.com](https://leetcode.com/problems/reshape-the-matrix/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/reshape-the-matrix
    ## Baisc Ideas:  If r*c != count of original matrix, we can't reshape it.
    ##               Trasverse the original matrix, and use index as a counter.
    ##               (i2, j2) is the position of the new matrix
    ##               i2 = index/c, j2 = index%c
    ##
    ## Complexity: Time O(n*m), Space O(1)
    class Solution(object):
        def matrixReshape(self, nums, r, c):
            """
            :type nums: List[List[int]]
            :type r: int
            :type c: int
            :rtype: List[List[int]]
            """
            row_count = len(nums)
            if row_count == 0: return nums
            col_count = len(nums[0])
            if r*c != row_count*col_count: return nums
            res = [None]*r
            for i in xrange(r): res[i] = [None]*c
            index = 0
            for i in xrange(row_count):
                for j in xrange(col_count):
                    i2 = index/c
                    j2 = index%c
                    res[i2][j2] = nums[i][j]
                    index += 1
            return res