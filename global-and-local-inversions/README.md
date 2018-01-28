# Leetcode: Global and Local Inversions     :BLOG:Amusing:


---

Global and Local Inversions  

---

Similar Problems:  
-   Tag: [#basic](http://brain.dennyzhang.com/tag/basic)

---

We have some permutation A of [0, 1, &#x2026;, N - 1], where N is the length of A.  

The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].  

The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].  

Return true if and only if the number of global inversions is equal to the number of local inversions.  

Example 1:  

    Input: A = [1,0,2]
    Output: true
    Explanation: There is 1 global inversion, and 1 local inversion.

    Example 2:
    
    Input: A = [1,2,0]
    Output: false
    Explanation: There are 2 global inversions, and 1 local inversion.

Note:  

-   A will be a permutation of [0, 1, &#x2026;, A.length - 1].
-   A will have length in range [1, 5000].
-   The time limit for this problem has been reduced.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/global-and-local-inversions)  

Credits To: [leetcode.com](https://leetcode.com/problems/global-and-local-inversions/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: http://brain.dennyzhang.com/global-and-local-inversions
    ## Basic Ideas: 
    ##      If both equals, apparently only the adjacent nodes can be in descedning order.
    ##      And their absolute difference should be only 1.
    ##      Why?
    ##      Let's examine, whether below is possible?
    ##           .   5  3 . . .
    ##         part1       part2 
    ##
    ##         Where we can put 4? 
    ##           If part1, the pair of 4 and 3 is only global inversions but not local ones.
    ##           If part2, the pair of 5 and 4 is only global inversions but not local ones.
    ##
    ##      On the other side, let's say the descedning pairs are adjacent nodes.
    ##      Then global inversions must equals local inversions.
    ## Complexity:
    class Solution(object):
        def isIdealPermutation(self, A):
            """
            :type A: List[int]
            :rtype: bool
            """
            length = len(A)
            if length <= 1: return True
            stack = []
            l = [-1] * length
            for i in range(0, length-1):
                if A[i+1] == A[i]+1:
                    continue
                # swap
                if A[i+1] == A[i]-1:
                    A[i],A[i+1] = A[i+1],A[i]
    
            for i in xrange(length):
                if A[i] != i: return False
            return True
    
    s = Solution()
    print s.isIdealPermutation([2,0,1]) # false
    print s.isIdealPermutation([1,0,2]) # true
    print s.isIdealPermutation([1,2,0]) # false
    print s.isIdealPermutation([0,2,1]) # true
    print s.isIdealPermutation([]) # true