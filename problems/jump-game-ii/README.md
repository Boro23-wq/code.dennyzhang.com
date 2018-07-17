
# Leetcode: Jump Game II     :BLOG:Hard:

---

Jump Game II  

---

Given an array of non-negative integers, you are initially positioned at the first index of the array.  

Each element in the array represents your maximum jump length at that position.  

Your goal is to reach the last index in the minimum number of jumps.  

For example:  
Given array A = [2,3,1,1,4]  

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)  

Note:  
You can assume that you can always reach the last index.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/jump-game-ii)  

Credits To: [leetcode.com](https://leetcode.com/problems/jump-game-ii/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/jump-game-ii
    import sys
    class Solution:
        ## Basic Ideas: greedy
        ##      maxIndex
        ##      preMaxIndex
        ## Complexity: Time O(n), Space O(n)
        def jump(self, nums):
    	"""
    	:type nums: List[int]
    	:rtype: int
    	"""
    	length = len(nums)
    	if length <= 1: return 0
    	maxIndex, preMaxIndex, steps = 0, 0, 0
    	minSteps = sys.maxsize
    	for i in range(0, length-1):
    	    # print(i, maxIndex, preMaxIndex, length, steps, minSteps)
    	    # we can't jump anymore
    	    if i > maxIndex: break
    	    # all elements in current level has been examined
    	    if i > preMaxIndex:
    		steps += 1
    		preMaxIndex = maxIndex
    	    if maxIndex < i+nums[i]:
    		maxIndex = i+nums[i]
    	    # already found the target
    	    if maxIndex >= length-1:
    		minSteps = min(minSteps, steps+1)
    	return minSteps
    
    # s = Solution()
    # print(s.jump([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3])) # 2
    # print(s.jump([2,3,1,1,4])) # 2

