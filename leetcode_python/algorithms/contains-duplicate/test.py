#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags:
## Description:
##     https://leetcode.com/problems/contains-duplicate/description/
## ,-----------
## | Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
## | 
## `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-11-12 10:05:23>
##-------------------------------------------------------------------
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ## Idea: Use set, then compare the count
        ## Complexity: Time ?, Space O(n)
        return len(set(nums)) != len(nums)

    def containsDuplicate1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ## Idea: Sort the list. Then check the adjancent items.
        ## Complexity: Time O(n*log(n)), Space O(1)
        nums2 = sorted(nums)
        length = len(nums2)
        if length < 2:
            return False

        for i in range(0, length-1):
            if nums2[i] == nums2[i+1]:
                return True
        return False
