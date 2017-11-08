#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Tags: #amusing
## Description:
##     https://leetcode.com/problems/add-two-numbers-ii/description/
##    ,-----------
##    | You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
##    | 
##    | You may assume the two numbers do not contain any leading zero, except the number 0 itself.
##    | 
##    | Follow up:
##    | What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
##    | 
##    | Example:
##    | 
##    | Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
##    | Output: 7 -> 8 -> 0 -> 7
##    `-----------
##
##
## Basic Idea:
## Complexity:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:16>
##-------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ## Idea:
        ##           add l2 to l1 without carry. has_carry(bool). If yes, keep checking l1
        ## Complexity: Time O(n*n), Space O(1)
        dummy1, dummy2 = ListNode(0), ListNode(0)
        dummy1.next, dummy2.next = l1, l2
        len1, len2 = 0, 0
        p = dummy1.next
        while(p):
            len1 += 1
            p = p.next

        q = dummy2.next
        while(q):
            len2 += 1
            q = q.next

        head, p, q = None, None, None
        # longer list
        if len1>=len2:
            head = dummy1
            p = dummy1.next
            q = dummy2.next
        else:
            head = dummy2
            p = dummy2.next
            q = dummy1.next
        
        # add short list into the long list
        for i in xrange(abs(len2-len1)):
            p = p.next

        has_carry = False
        while p:
            p.val += q.val
            if p.val >= 10:
                has_carry = True
            p = p.next
            q = q.next

        while has_carry:
            p = head
            has_carry = False
            while(p.next):
                if p.next.val >= 10:
                    p.val += 1
                    if p.val >= 10:
                        has_carry = True
                    p.next.val = p.next.val % 10
                p = p.next

        return head.next if head.val == 0 else head
        