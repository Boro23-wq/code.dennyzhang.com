# Leetcode: 132 Pattern     :BLOG:Medium:


---

Check whether 132 pattern exists in the given array  

---

Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.  

Note: n will be less than 15,000.  

    Example 1:
    Input: [1, 2, 3, 4]
    
    Output: False
    
    Explanation: There is no 132 pattern in the sequence.

    Example 2:
    Input: [3, 1, 4, 2]
    
    Output: True
    
    Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

    Example 3:
    Input: [-1, 3, 2, 0]
    
    Output: True
    
    Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/132-pattern)  

Credits To: [leetcode.com](https://leetcode.com/problems/132-pattern/description/)  

Leave me comments, if you know how to solve.  

[Hints](#c7254e):  

    ## Blog link: http://brain.dennyzhang.com/132-pattern
    ## Basic Ideas: There should be one rise. After that, there should be one drop.
    ## Complexity: Time O(n), Space O(1)
    ## Scenario: sell sock at a high price

    class Solution(object):
        def find132pattern(self, nums):
            """
            :type nums: List[int]
            :rtype: bool
            """
            length = len(nums)
            if length < 3:
                return False
            has_rise, has_drop = False, False
            for i in range(1, length):
                if nums[i] > nums[i-1]:
                    has_rise = True
                if has_rise and nums[i] < nums[i-1]:
                    has_drop = True
                if has_rise and has_drop:
                    return True
            return has_rise and has_drop
    
    s = Solution()
    print s.find132pattern([1, 2, 3, 4])
    print s.find132pattern([3, 1, 4, 2])
    print s.find132pattern([-1, 3, 2, 0])