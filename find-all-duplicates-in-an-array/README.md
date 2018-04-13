# Leetcode: Find All Duplicates in an Array     :BLOG:Basic:


---

Identify duplicates in a list of numbers  

---

Given an array of integers, 1 <= a[i] <= n (n = size of array), some elements appear twice and others appear once.  

Find all the elements that appear twice in this array.  

Could you do it without extra space and in O(n) runtime?  

Example:  

    Input:
    [4,3,2,7,8,2,3,1]
    
    Output:
    [2,3]

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/find-all-duplicates-in-an-array)  

Credits To: [leetcode.com](https://leetcode.com/problems/find-all-duplicates-in-an-array/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/find-all-duplicates-in-an-array
    ## Basic Ideas: count sort
    ## Complexity: Time O(n), Space (1)
    ##   1 2 3 4 5 6 7 8
    ##   4 3 2 7 8 2 3 2
    ##     2 3 4     7
    class Solution(object):
        def findDuplicates(self, nums):
            """
            :type nums: List[int]
            :rtype: List[int]
            """
            i = 0
            length = len(nums)
            if length < 2:
                return []
    
            while i < length:
                # move to next if in position or the same
                if nums[i] - 1 == i or nums[i] == nums[nums[i] - 1]:
                    i = i + 1
                else:
                    j = nums[i] - 1
                    # swap nums[i] and nums[j]
                    nums[i], nums[j] = nums[j], nums[i]
            res = []
            for i in xrange(length):
                if nums[i]  != i+1:
                    res.append(nums[i])
            return res