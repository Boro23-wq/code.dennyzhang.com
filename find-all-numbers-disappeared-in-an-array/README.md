# Leetcode: Find All Numbers Disappeared in an Array     :BLOG:Basic:


---

Find missing numbers  

---

Given an array of integers where 1 <= a[i] <= n (n = size of array), some elements appear twice and others appear once.  

Find all the elements of [1, n] inclusive that do not appear in this array.  

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.  

Example:  

    Input:
    [4,3,2,7,8,2,3,1]
    
    Output:
    [5,6]

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/find-all-numbers-disappeared-in-an-array)  

Credits To: [leetcode.com](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/find-all-numbers-disappeared-in-an-array
    ## Basic Ideas: traverse each item
    ## Complexity:
    ##  1,2,3,4,5,6,7,8
    ##
    ##  4,3,2,7,8,2,3,1
    ##  1,2,3,4,    7,8
    class Solution(object):
        def findDisappearedNumbers(self, nums):
            """
            :type nums: List[int]
            :rtype: List[int]
            """
            for i in range(0, len(nums)):
                value = nums[i]
                if (value == i+1):
                    continue
    
                while (nums[value-1] != value):
                    tmp = nums[value-1]
                    nums[value-1] = value
                    value = tmp
    
            ret = []
            for i in range(0, len(nums)):
                if nums[i] != (i+1):
                    ret.append(i+1)
            return ret