# Leetcode: Line Reflection     :BLOG:Medium:


---

Line Reflection  

---

Similar Problems:  
-   [Tag: #set](https://code.dennyzhang.com/tag/set)

---

Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points.  

Example 1:  

    Given points = [[1,1],[-1,1]], return true.

Example 2:  

    Given points = [[1,1],[-1,-1]], return false.

Follow up:  
Could you do better than O(n^2)?  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/line-reflection)  

Credits To: [leetcode.com](https://leetcode.com/problems/line-reflection/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/line-reflection
    ## Basic Ideas: set
    ##   Find the min and max x, then we get a line
    ##   All points should be mirrored with this line.
    ##     [(0, 1), (0, 1)]: false
    ##     [(0, 1), (0, 2)]: false
    ##     [(0, 0)]: true
    ## Complexity: Time O(n), Space O(n)
    class Solution:
        def isReflected(self, points):
            """
            :type points: List[List[int]]
            :rtype: bool
            """
            import sys
            if len(points) == 0: return True
            s, s_removed = set([]), set([])
            min_x, max_x = sys.maxsize, -sys.maxsize-1
            for [x, y] in points:
                if x<min_x: min_x = x
                if x>max_x: max_x = x
            mirror_x = (min_x+max_x)/2
    
            for [x, y] in points:
                if x == mirror_x: continue
                if (x, y) in s_removed: continue
                if (2*mirror_x-x, y) in s:
                    s.remove((2*mirror_x-x, y))
                    s_removed.add((2*mirror_x-x, y))
                    s_removed.add((x, y))
                else:
                    s.add((x, y))
            return len(s) == 0