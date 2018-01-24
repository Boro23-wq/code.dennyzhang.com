# Leetcode: Missing Number     :BLOG:Amusing:


---

Identity the missing number  

---

Given an array containing n distinct numbers taken from 0, 1, 2, &#x2026;, n, find the one that is missing from the array.  

    Example 1
    
    Input: [3,0,1]
    Output: 2

    Example 2
    
    Input: [9,6,4,2,3,5,7,0,1]
    Output: 8

Note:  
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/missing-number)  

Credits To: [leetcode.com](https://leetcode.com/problems/missing-number/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: http://brain.dennyzhang.com/missing-number
    class Solution(object):
        def missingNumber(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            ## Idea: Use xor
            ## Complexity: Time O(n), Space O(1)
            n = len(nums)
            xor_value = 0
            for i in range(0, n):
                xor_value = xor_value ^ (i+1) ^ nums[i]
    
            return xor_value
    
        def missingNumber2(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            ## Idea: Use xor
            ## Complexity: Time O(n), Space O(1)
            n = len(nums)
            xor_value = 0
            for i in range(0, n+1):
                xor_value = xor_value ^ i
    
            for i in range(0, n):
                xor_value = xor_value ^ nums[i]
            return xor_value
    
        def missingNumber1(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            ## Idea: caculated the desired sum. Then add up all the numbers. Do the substraction.
            ## Complexity: Time O(n), Space O(1)
            n = len(nums)
            supposed_sum = (n * (n+1))/2
            for i in range(0, n):
                supposed_sum -= nums[i]
            return supposed_sum