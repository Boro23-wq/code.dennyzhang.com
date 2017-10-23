#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description:
##     https://leetcode.com/problems/number-of-1-bits/description/
## Basic Idea:
## Complexity:
## Tags:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-23 18:22:05>
##-------------------------------------------------------------------
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n != 0:
            if (n % 2) == 1:
                count = count + 1
            n = n /2
        return count
            
if __name__ == '__main__':
    s = Solution()
    print s.hammingWeight(3) # 2
    print s.hammingWeight(4) # 1
## File: test.py ends
