# Leetcode: Contains Duplicate II     :BLOG:Medium:


---

Contains Duplicate II  

---

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/contains-duplicate-ii)  

Credits To: [Leetcode.com](https://leetcode.com/problems/contains-duplicate-ii/description/)  

Leave me comments, if you know how to solve.  

    ## Baisc Ideas: sliding window
    ##              Keep a window of k+1 elements. Maintain a Set with the window
    ##              Move the window towards the end.
    ##              If found an existing
    ##
    ## Complexity: Time O(n), Space O(k)
    class Solution(object):
        def containsNearbyDuplicate(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: bool
            """
            length = len(nums)
            if length <= 1:
                return False
            if k == 0:
                return False
    
            set_list = set()
            index = min(k+1, length)
            # build sliding window from nums[0:index]
            for i in range(0, index):
                set_list.add(nums[i])
    
            # duplicate is found in the initial window
            if len(set_list) != index:
                return True
    
            # move the sliding window to the right
            for i in range(index, length):
                set_list.remove(nums[i-index])
                if nums[i] in set_list:
                    return True
                set_list.add(nums[i])
            return False
    
    s = Solution()
    print s.containsNearbyDuplicate([-1, -1], 1) # True
    print s.containsNearbyDuplicate([99, 99], 1) # True
    print s.containsNearbyDuplicate([1, 2, 1], 0) # False