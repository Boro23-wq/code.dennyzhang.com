# Leetcode: Relative Ranks     :BLOG:Amusing:


---

Relative Ranks  

---

Given an integer array of size n, find all elements that appear more than n/3 times. The algorithm should run in linear time and in O(1) space.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/relative-ranks)  

Credits To: [leetcode.com](https://leetcode.com/problems/relative-ranks/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: http://brain.dennyzhang.com/relative-ranks
    ## Basic Ideas:
    ##           Sort the list. Build a map. key(score): value(position in sorted list)
    ##           Trasverse the original list again, get the position by map
    ## Complexity: Time O(n*log(n)), Space O(n)
    class Solution(object):
        def findRelativeRanks(self, nums):
            """
            :type nums: List[int]
            :rtype: List[str]
            """
            score_nums = sorted(nums)
            score_nums.reverse()
            m = {}
            for i in xrange(len(score_nums)):
                m[score_nums[i]] = i
    
            res = []
            for num in nums:
                rank = m[num]
                if rank == 0: element = 'Gold Medal'
                elif rank == 1: element = 'Silver Medal'
                elif rank == 2: element = 'Bronze Medal'
                else: element = str(rank+1)
                res.append(element)
            return res