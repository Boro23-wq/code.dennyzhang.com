#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description:
##     https://leetcode.com/problems/judge-route-circle/description/
## Basic Idea:
## Tags:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-23 16:55:15>
##-------------------------------------------------------------------
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = 0
        y = 0
        for move in moves:
            if move not in 'UDLR':
                raise Exception("Wrong move: %s" % (move))

            if move == 'U':
                y += 1
            if move == 'D':
                y -= 1
            if move == 'L':
                x -= 1
            if move == 'R':
                x += 1
        return (x == 0) and (y==0)

if __name__ == '__main__':
    s = Solution()
    print s.judgeCircle("UD")
    print s.judgeCircle("LL")
## File: test.py ends
