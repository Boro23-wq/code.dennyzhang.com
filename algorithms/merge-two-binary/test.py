#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Tags:
## Description:
##     https://leetcode.com/problems/merge-two-binary-trees/description/
## Basic Idea:
## Complexity:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:17>
##-------------------------------------------------------------------
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        i = 0
        for n in nums:
            d[n]= i
            i = i + 1

        i = 0
        while i<target:
            if d.has_key(target - (i+1)):
                return [i, d[target-i-1]]
                break
            i = i + 1
        return [None, None]

if __name__ == '__main__':
    s = Solution()
    print s.twoSum([1, 2, 3], 5)
    print s.twoSum([2, 7, 11, 15], 9)
## File: test.py ends
