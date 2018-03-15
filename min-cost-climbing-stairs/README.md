# Leetcode: Min Cost Climbing Stairs     :BLOG:Basic:


---

Min Cost Climbing Stairs  

---

Similar Problems:  
-   [Review: Dynamic Programming Problems](https://brain.dennyzhang.com/review-dynamicprogramming), [Tag: #dynamicprogramming](https://brain.dennyzhang.com/tag/dynamicprogramming)

---

On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).  

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.  

    Example 1:
    Input: cost = [10, 15, 20]
    Output: 15
    Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

    Example 2:
    Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    Output: 6
    Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].

Note:  
1.  cost will have a length in the range [2, 1000].
2.  Every cost[i] will be an integer in the range [0, 999].

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/min-cost-climbing-stairs)  

Credits To: [leetcode.com](https://leetcode.com/problems/min-cost-climbing-stairs/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/min-cost-climbing-stairs
    ## Basic Ideas:
    ##       Facts: you can only climb one or two steps. But you can't climb back.
    ##
    ##           0     1     2
    ##          10    15    20
    ##
    ##          There are only two cases to reach n, either from n-1 or n-2
    ##                f(n) = min(f(n-1)+cost[n-1], f(n-2)+cost[n-2])
    ##     Attention: The target we want to reach is not the last element. But the element after last element
    ##
    ## Complexity: Time O(n), Space O(1)
    class Solution(object):
        # Improvement: we don't need list to save the result.
        #              It will only involve two of previous result.
        def minCostClimbingStairs(self, cost):
            """
            :type cost: List[int]
            :rtype: int
            """
            n = len(cost)
            if n == 0: return 0
            if n == 1: return 0
            ## prev1, prev2, ... i
            prev1, prev2 = 0, 0
            # calculate from 2 to n
            for i in range(2, n+1):
                prev2, prev1 = min(prev1+cost[i-2], prev2+cost[i-1]), prev2
            # prev2 would be the position after last position
            # prev1 is the value of last position
            return prev2
    
        def minCostClimbingStairs_v1(self, cost):
            """
            :type cost: List[int]
            :rtype: int
            """
            n = len(cost)
            if n == 0: return 0
            if n == 1: return 0
            l = [None]*(n+1)
            l[1]=l[0]=0
            for i in range(2, n+1):
                l[i] = min(l[i-1]+cost[i-1], l[i-2]+cost[i-2])
            return l[n]
    
    # s = Solution()
    # print s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) # 6