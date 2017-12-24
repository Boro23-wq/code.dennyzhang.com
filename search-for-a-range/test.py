#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 brain.dennyzhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags: #redo, #todobrain
## Description:
##     https://leetcode.com/problems/search-for-a-range/description/
##    ,-----------
##    | Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.
##    | 
##    | Your algorithm's runtime complexity must be in the order of O(log n).
##    | 
##    | If the target is not found in the array, return [-1, -1].
##    | 
##    | For example,
##    | Given [5, 7, 7, 8, 8, 10] and target value 8,
##    | return [3, 4].
##    | 
##    `-----------
##    
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-24 17:21:30>
##-------------------------------------------------------------------
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ## Basic Idea: binary search
        ## Complexity: Time O(log(n)), Space O(1)
        ## Assumptions:
        ## Sample Data:
        ##    5, 7, 7, 8, 8, 10
        ##             8
        ## binary search: 3 cases of not found
        ##           right mid(left)
        ##                mid(right) left
        length = len(nums)
        left, right = 0, length - 1
        while left <= right:
            mid = left + (right-left)/2
            if nums[mid] >= target:
                # left half
                right = mid - 1
            else:
                left = mid + 1

        # print("round1 mid: %d, left: %d, right: %d. nums: %s" % (mid, left, right, nums))

        left_index = min(left, right) + 1
        if left_index >= length:
            return [-1, -1]
        if nums[left_index] != target:
            return [-1, -1]

        left, right = 0, length - 1
        while left <= right:
            mid = left + (right-left)/2
            if nums[mid] <= target:
                # right half
                left = mid + 1
            else:
                right = mid - 1

        # print("round2 mid: %d, left: %d, right: %d. nums: %s" % (mid, left, right, nums))
        right_index = min(left, right)
        return [left_index, right_index]

s = Solution()
print s.searchRange([5,7,7,8,8,8,10], 8)
