# Leetcode: Jump Game     :BLOG:Basic:


---

Jump Game  

---

Given an array of non-negative integers, you are initially positioned at the first index of the array.  

Each element in the array represents your maximum jump length at that position.  

Determine if you are able to reach the last index.  

For example:  

    A = [2,3,1,1,4], return true.
    
    A = [3,2,1,0,4], return false.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/jump-game)  

Credits To: [leetcode.com](https://leetcode.com/problems/jump-game/description/)  

Leave me comments, if you have better ways to solve.  

Interesting reading:  
[YouTube Coding Interview Question: Tower Hopper Problem](https://www.youtube.com/watch?v=kHWy5nEfRIQ&list=PLBZBJbE_rGRVnpitdvpdY9952IsKMDuev&index=11)  

    ## Blog link: https://brain.dennyzhang.com/jump-game
    ## Basic Ideas:
    ##        maxIndex: keep tracking the furthest reachable index
    ##
    ## Complexity: Time O(n), Space O(1)
    class Solution:
        def canJump(self, nums):
            """
            :type nums: List[int]
            :rtype: bool
            """
            length = len(nums)
            if length <= 1: return True
            maxIndex = 0
            for i in range(0, length-1):
                # we can't jump anymore
                if i > maxIndex: break
                # already found the target
                if maxIndex >= length-1: break
                maxIndex = max(maxIndex, i+nums[i])
            return maxIndex >= length-1
    
    # s = Solution()
    # print(s.canJump([0, 2, 3])) # False