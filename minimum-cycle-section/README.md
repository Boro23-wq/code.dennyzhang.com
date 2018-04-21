# Leetcode: Minimum Cycle Section     :BLOG:Hard:


---

Minimum Cycle Section  

---

Similar Problems:  
-   Tag: [#dynamicprogramming](https://code.dennyzhang.com/tag/dynamicprogramming)

---

Given an array of int, find the length of the minimum cycle section.  

 Notice  
The length of array do not exceed 100000.  
Each element is in the int range  

Example  

    Given array = [1,2,1,2,1,2], return 2.
    
    Explanation:
    The minimum cycle section is [1,2], and the length is 2.

    Given array = [1,2,1,2,1], return 2.
    
    Explanation:
    The minimum cycle section is [1,2], and the length is 2, although the last 2 is not given, we still consider the cycle section is [1,2].

    Given array = [1,2,1,2,1,4], return 6.
    
    Explanation:
    The minimum cycle section is [1,2,1,2,1,4], and the length is 6.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/minimum-cycle-section)  

Credits To: [lintcode.com](http://www.lintcode.com/en/problem/minimum-cycle-section/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/minimum-cycle-section
    class Solution:
        """
        @param array: an integer array
        @return: the length of the minimum cycle section
        """
        def minimumCycleSection(self, array):
            ## Basic Ideas: Dynamic programming
            ##  dp(i) = dp(i-1), if array[i] == array[i-dp(i-1)]
            ##          i+1, otherwise
            ## Complexity: Time O(n), Space O(n)
            length = len(array)
            if length <= 1: return length
            dp = [0 for i in range(length)]
            dp[0] = 1
            for i in range(1, length):
                if array[i] == array[i-dp[i-1]]:
                    dp[i] = dp[i-1]
                else:
                    if array[i] == array[0]:
                        dp[i] = i
                    else: 
                        dp[i] = i+1
            return dp[-1]