# Leetcode: First Bad Version     :BLOG:Basic:


---

First Bad Version  

---

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.  

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.  

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/first-bad-version)  

Credits To: [Leetcode.com](https://leetcode.com/problems/first-bad-version/description/)  

Leave me comments, if you know how to solve.  

    ## Basic Ideas: Binary search
    ##              Find the first False
    ## Complexity: Time O(log(n)), Space O(1)
    
    # The isBadVersion API is already defined for you.
    # @param version, an integer
    # @return a bool
    # def isBadVersion(version):
    
    class Solution(object):
        def firstBadVersion(self, n):
            """
            :type n: int
            :rtype: int
            """
            left, right = 1, n
            while left <= right:
                mid = left + (right-left)/2
                if isBadVersion(mid) is False:
                    left = mid + 1
                else:
                    if mid == 1:
                        return 1
                    if isBadVersion(mid-1) is False:
                        return mid
                    else:
                        right = mid - 1
            return mid if isBadVersion(mid) else None