#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Description:
##     https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
##    ,-----------
##    | Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
##    | 
##    | Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
##    | 
##    | The order of output does not matter.
##    | 
##    | Example 1:
##    | 
##    | Input:
##    | s: "cbaebabacd" p: "abc"
##    | 
##    | Output:
##    | [0, 6]
##    | 
##    | Explanation:
##    | The substring with start index = 0 is "cba", which is an anagram of "abc".
##    | The substring with start index = 6 is "bac", which is an anagram of "abc".
##    | Example 2:
##    | 
##    | Input:
##    | s: "abab" p: "ab"
##    | 
##    | Output:
##    | [0, 1, 2]
##    | 
##    | Explanation:
##    | The substring with start index = 0 is "ab", which is an anagram of "ab".
##    | The substring with start index = 1 is "ba", which is an anagram of "ab".
##    | The substring with start index = 2 is "ab", which is an anagram of "ab".
##    `-----------
##    
## Basic Idea:
## Complexity:
## Tags: #redo
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-23 18:22:06>
##-------------------------------------------------------------------
class Solution(object):
    def is_same_dict(self, dict_1, dict_2):
        has_matched = True
        if len(dict_1.keys()) == len(dict_2.keys()):
            for k in dict_1:
                if dict_1[k] != dict_2[k]:
                    has_matched = False
                    break
        else:
            has_matched = False

        return has_matched

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        p_dict = {}
        q_dict = {}
        ret = []

        if len(s) < len(p):
            return []

        for ch in 'abcdefghijklmnopqrstuvwxyz':
            p_dict[ch] = 0
        for ch in p:
            p_dict[ch] += 1

        for ch in 'abcdefghijklmnopqrstuvwxyz':
            q_dict[ch] = 0
        for ch in s[0:len(p)]:
            q_dict[ch] += 1

        if self.is_same_dict(p_dict, q_dict) is True:
            ret.append(0)

        # loop the change
        for i in range(1, len(s)-len(p)+1):
            # print q_dict
            q_dict[s[i+len(p)-1]] += 1
            q_dict[s[i-1]] -= 1
            if self.is_same_dict(p_dict, q_dict) is True:
                ret.append(i)

        return ret

if __name__ == '__main__':
    s = Solution()
    print s.findAnagrams("abab", "ab")
    print s.findAnagrams("cbaebabacd", "abc")
## File: test.py ends
