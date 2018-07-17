
# Leetcode: First Missing Positive     :BLOG:Hard:

---

Find first positive integer  

---

Given an unsorted integer array, find the first missing positive integer.  

    For example,
    Given [1,2,0] return 3,
    and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/first-missing-positive)  

Credits To: [leetcode.com](https://leetcode.com/problems/first-missing-positive/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/first-missing-positive
    ## Basic Ideas: count sort. Put each number in its right place.
    ##    Sample Data:
    ##    1  2  0
    ##    3  4  0  1
    ##    0  4  3  1
    ##    0  1  3  4
    ## Complexity:
    class Solution(object):
        def firstMissingPositive(self, nums):
    	"""
    	:type nums: List[int]
    	:rtype: int
    	"""
    	length = len(nums)
    	# set negative elements to 0s, and set elements bigger than length to 0s
    	for i in xrange(length):
    	    if nums[i] < 0 or nums[i] > length:
    		nums[i] = 0
    
    	i = 0
    	while i < length:
    	    j = nums[i] - 1
    	    if nums[i] == i+1 or nums[i] == 0 \
    	       or nums[i] == nums[j]:
    		i = i + 1
    	    else:
    		# swap
    		nums[i], nums[j] = nums[j], nums[i]
    
    	# get result
    	for i in xrange(length):
    	    if nums[i] != i+1:
    		return i+1
    	return length+1
    
    # s = Solution()
    # print s.firstMissingPositive([3,4,-1,1])

