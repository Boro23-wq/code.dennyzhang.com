# Leetcode: Escape The Ghosts     :BLOG:Amusing:


---

Escape The Ghosts  

---

Similar Problems:  
-   Tag: [#array](https://code.dennyzhang.com/tag/array)

---

You are playing a simplified Pacman game. You start at the point (0, 0), and your destination is (target, target). There are several ghosts on the map, the i-th ghost starts at (ghosts[i], ghosts[i]).  

Each turn, you and all ghosts simultaneously **may** move in one of 4 cardinal directions: north, east, west, or south, going from the previous point to a new point 1 unit of distance away.  

You escape if and only if you can reach the target before any ghost reaches you (for any given moves the ghosts may take.)  If you reach any square (including the target) at the same time as a ghost, it doesn't count as an escape.  

Return True if and only if it is possible to escape.  

Example 1:  

    Input: 
    ghosts = [[1, 0], [0, 3]]
    target = [0, 1]
    Output: true
    Explanation: 
    You can directly reach the destination (0, 1) at time 1, while the ghosts located at (1, 0) or (0, 3) have no way to catch up with you.

Example 2:  

    Input: 
    ghosts = [[1, 0]]
    target = [2, 0]
    Output: false
    Explanation: 
    You need to reach the destination (2, 0), but the ghost at (1, 0) lies between you and the destination.

Example 3:  

    Input: 
    ghosts = [[2, 0]]
    target = [1, 0]
    Output: false
    Explanation: 
    The ghost can reach the target at the same time as you.

Note:  

-   All points have coordinates with absolute value <= 10000.
-   The number of ghosts will not exceed 100.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/escape-the-ghosts)  

Credits To: [leetcode.com](https://leetcode.com/problems/escape-the-ghosts/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/escape-the-ghosts
    ## Basic Ideas: Get the minimum distance
    ##
    ## Complexity: Time O(1), Space O(1)
    class Solution:
        def escapeGhosts(self, ghosts, target):
            """
            :type ghosts: List[List[int]]
            :type target: List[int]
            :rtype: bool
            """
            my_distance = abs(target[0]) + abs(target[1])
    
            for ghost in ghosts:
                distance = abs(ghost[0]-target[0]) + abs(ghost[1]-target[1])
                if distance <= my_distance: return False
            return True

<div id="footnotes">
<h2 class="footnotes">Footnotes: </h2>
<div id="text-footnotes">

<div class="footdef"><sup><a id="fn.1" name="fn.1" class="footnum" href="#fnr.1">1</a></sup> <p>DEFINITION NOT FOUND.</p></div>

<div class="footdef"><sup><a id="fn.2" name="fn.2" class="footnum" href="#fnr.2">2</a></sup> <p>DEFINITION NOT FOUND.</p></div>


</div>
</div>