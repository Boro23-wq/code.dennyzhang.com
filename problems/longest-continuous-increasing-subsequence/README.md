# Leetcode: Longest Continuous Increasing Subsequence     :BLOG:Basic:


---

Longest Continuous Increasing Subsequence  

---

Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).  

    Example 1:
    Input: [1,3,5,4,7]
    Output: 3
    Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
    Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.

    Example 2:
    Input: [2,2,2,2,2]
    Output: 1
    Explanation: The longest continuous increasing subsequence is [2], its length is 1.

Note: Length of the array will not exceed 10,000.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/longest-continuous-increasing-subsequence)  

Credits To: [leetcode.com](https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/longest-continuous-increasing-subsequence
    ## Basic Ideas: array has been splited as sections with increasing subsequence
    ## 
    ##
    ## Complexity: Time O(n), Space O(1)
    class Solution:
        def findLengthOfLCIS(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            res, cnt = 0, 0
            for i in range(0, len(nums)):
                if i==0 or nums[i-1] < nums[i]:
                    cnt += 1
                    res = max(res, cnt)
                else:
                    cnt = 1
            return res
    
    # s = Solution()
    # print(s.findLengthOfLCIS([1,3,5,7])) # 4
    # print(s.findLengthOfLCIS([1,3,5,4,7])) # 3
    # print(s.findLengthOfLCIS([2,2,2,2])) # 1