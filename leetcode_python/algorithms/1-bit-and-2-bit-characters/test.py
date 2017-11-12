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
##     https://leetcode.com/problems/1-bit-and-2-bit-characters/description/
##    ,-----------
##    | We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).
##    | 
##    | Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.
##    | 
##    | Example 1:
##    | Input: 
##    | bits = [1, 0, 0]
##    | Output: True
##    | Explanation: 
##    | The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
##    | Example 2:
##    | Input: 
##    | bits = [1, 1, 1, 0]
##    | Output: False
##    | Explanation: 
##    | The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.
##    | Note:
##    | 
##    | 1 <= len(bits) <= 1000.
##    | bits[i] is always 0 or 1.
##    `-----------
##
##
## Basic Idea:
## Complexity:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:16>
##-------------------------------------------------------------------
class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        ## Idea: One pass
        ##       If current digit is 0, move 1 step
        ##       If current digit is 1, move 2 steps
        ##       Check whether the last match is 1 step
        ##       Note: since the last digit is 0, the given string can always match
        ## Complexity: Time O(n), Space O(1)
        length = len(bits)
        if length == 0:
            return False
        if length == 1:
            return bits[0] == 0

        i = 0
        while i< length:
            if bits[i] == 0:
                i += 1
            else:
                i += 2
            if i == length - 1:
                return True
        return False