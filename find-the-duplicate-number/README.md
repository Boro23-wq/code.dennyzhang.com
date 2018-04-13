# Leetcode: Find the Duplicate Number     :BLOG:Amusing:


---

Find the only one duplicate number  

---

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.  

Note:  
1.  You must not modify the array (assume the array is read only).
2.  You must use only constant, O(1) extra space.
3.  Your runtime complexity should be less than O(n\*n).
4.  There is only one duplicate number in the array, but it could be repeated more than once.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/find-the-duplicate-number)  

Credits To: [leetcode.com](https://leetcode.com/problems/find-the-duplicate-number/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/find-the-duplicate-number
    ## Basic Ideas: Binary search
    ##              The target is in [1, n]
    ##              Compare all elements with the value of n/2
    ##              Count how many elements equal the value, smaller than it
    ##              If more than 1 elements equal the value, we found the target
    ##              If too many elements smaller than the value, the target is in [1, n/2 -1].
    ##              Otherwise in [n/2+1, n]
    ##              So on and so forth. 
    ##              Once the interval narrow down to zero elements, the loop breaks.
    ##    Sample Data: n = 4
    ##               1 3 4 2 1
    ## Complexity: Time O(n*log(n)), Space O(1)
    class Solution(object):
        def findDuplicate(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            length = len(nums)
            left, right = 1, length - 1
            while left <= right:
                mid = left + (right-left)/2
                small, equal = 0, 0
                for num in nums:
                    if num == mid:
                        equal += 1
                    elif num < mid:
                        small += 1
                    # quick break
                    if equal > 1:
                        return num
    
                if small >= mid:
                    # left half
                    right = mid - 1
                else:
                    left = mid + 1
            return None
    
    # s = Solution()
    # print s.findDuplicate([1,3,4,2,1])