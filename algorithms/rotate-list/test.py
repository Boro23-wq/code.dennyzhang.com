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
##     https://leetcode.com/problems/rotate-list/description/
##    ,-----------
##    | Given a list, rotate the list to the right by k places, where k is non-negative.
##    | 
##    | For example:
##    | Given 1->2->3->4->5->NULL and k = 2,
##    | return 4->5->1->2->3->NULL.
##    `-----------
##
## Basic Idea:
##      1->2->3->4->5->NULL
##      1->2->3->    4->5->NULL
##    head    p      q  r
##
## Complexity:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:13>
##-------------------------------------------------------------------
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        p = head
        length = 1
        while p.next is not None:
            length += 1
            p = p.next

        k = k % length
        if k == 0:
            return head

        p = head
        for i in range(0, length-k-1):
            p = p.next

        q = p.next
        r = q
        while r.next is not None:
            r = r.next
        r.next = head
        p.next = None
        head = q
        return head
## File: test.py ends
