#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description :
##     https://leetcode.com/problems/reverse-integer/description/
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-20 17:19:26>
##-------------------------------------------------------------------
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = 0
        if x == 0:
            return x

        is_negative = (x<0)

        if is_negative is True:
            x = -x

        while x != 0:
            y = y*10 + (x % 10)
            x = x/10

        if is_negative is True:
            return -y
        else:
            return y
            
if __name__ == '__main__':
    s = Solution()
    print s.reverse(0)
    print s.reverse(123)
    print s.reverse(-123)
## File: test.py ends
