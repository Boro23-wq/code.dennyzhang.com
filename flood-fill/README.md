# Leetcode: Flood Fill     :BLOG:Basic:


---

Flood Fill  

---

An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).  

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.  

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.  

At the end, return the modified image.  

    Example 1:
    Input: 
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1, sc = 1, newColor = 2
    Output: [[2,2,2],[2,2,0],[2,0,1]]
    Explanation: 
    From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
    by a path of the same color as the starting pixel are colored with the new color.
    Note the bottom corner is not colored 2, because it is not 4-directionally connected
    to the starting pixel.

Note:  

    - The length of image and image[0] will be in the range [1, 50].
    - The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
    - The value of each color in image[i][j] and newColor will be an integer in [0, 65535].

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/flood-fill)  

Credits To: [leetcode.com](https://leetcode.com/problems/flood-fill/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/flood-fill
    ## Basic Ideas: dfs
    ##              If the position we checked doesn't have the original value, stop
    ##              Otherwise mark it as the new value, and search 4 directions.
    ##
    ## Complexity: Time O(n*m), Space O(1)
    ##             Why the time complexity is O(n*m)? 
    ##             Since the marked positions won't be visisted, so it's one pass.
    ##             To be more accurate, it's the region which need to be updated
    class Solution(object):
        def floodFill(self, image, sr, sc, newColor):
            """
            :type image: List[List[int]]
            :type sr: int
            :type sc: int
            :type newColor: int
            :rtype: List[List[int]]
            """
            self.row_count = len(image)
            if self.row_count == 0: return image
            self.col_count = len(image[0])
            if sr < 0 or sr >= self.row_count or \
                sc < 0 or sc >= self.col_count:
                    return image
            oldColor = image[sr][sc]
            if oldColor != newColor:
                self.DFSMark(image, sr, sc, oldColor, newColor)
            return image
    
        def DFSMark(self, image, i, j, oldColor, newColor):
            if i < 0 or i >= self.row_count or \
                j < 0 or j >= self.col_count:
                    return
            if image[i][j] != oldColor:
                return
            image[i][j] = newColor
            self.DFSMark(image, i-1, j, oldColor, newColor)
            self.DFSMark(image, i+1, j, oldColor, newColor)
            self.DFSMark(image, i, j-1, oldColor, newColor)
            self.DFSMark(image, i, j+1, oldColor, newColor)