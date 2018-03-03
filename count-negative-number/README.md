# LintCode: Count Negative Number     :BLOG:Medium:


---

Count Negative Number  

---

Similar Problems:  

-   [Search a 2D Matrix II](https://brain.dennyzhang.com/search-a-2d-matrix-ii)
-   [Review: Binary Search Problems](https://brain.dennyzhang.com/review-binarysearch), [Tag: #binarysearch](https://brain.dennyzhang.com/tag/binarysearch)

---

Give a horizontally sorted and vertically sorted n \* m matrix, find the number of negative number.  

 Notice  
The size of given matrix is n x m, n <= 500, m <= 500.  
In order to restrain the time complexity of the program, your program will run 10 ^ 5 times.  
Have you met this question in a real interview?  
Example  

    Given mat =
    
    [
        [-5,-3,-1,0,1],
        [-2,-1,0,0,1],
        [0,11,12,12,14]
    ],
    return 5.

    Explanation:
    There are only 5 negative number.
    Given mat =
    
    [
        [-50,-30,-10,-5],
        [-30,-20,-5,-1],
        [-10,-5,-1,0]
    ]
    return 11。
    
    Explanation:
    There are only 11 negative number.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/example)  

Credits To: [LintCode.com](http://www.lintcode.com/en/problem/count-negative-number/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/example
    class Solution:
        """
        @param nums: the sorted matrix
        @return: the number of Negative Number
        """
        def countNumber(self, nums):
            ## Basic Ideas:
            ## Complexity: Time O(n*log(m)), Space O(1)
            row_count = len(nums)
            if row_count == 0: return 0
            col_count = len(nums[0])
    
            res = 0
    
            left = max(self.findFirstNegative(nums[-1], 0, col_count-1), 0)
            i, j = 0, col_count-1
            while i>=0 and i<=row_count-1 and \
                j>=0 and j<=col_count-1:
                if nums[i][j] >= 0:
                    j = self.findFirstNegative(nums[i], left, j)
                res += j+1
                i += 1
            return res
    
        def findFirstNegative(self, myList, left, right):
            l, r = left, right
            while l<r:
                mid = l + int((r-l)/2)
                # find first non-negative
                if myList[mid] >= 0:
                    r = mid
                else:
                    l = mid + 1
            return l if myList[l]<0 else l-1