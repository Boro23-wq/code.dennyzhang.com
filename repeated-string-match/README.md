# Leetcode: Repeated String Match     :BLOG:Medium:


---

Repeated String Match  

---

Similar Problems:  
-   [Rotate String](https://brain.dennyzhang.com/rotate-string)
-   Tag: [#string](https://brain.dennyzhang.com/tag/string), [#rotateoperation](https://brain.dennyzhang.com/tag/rotateoperation)

---

Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.  

For example, with A = "abcd" and B = "cdabcdab".  

Return 3, because by repeating A three times ("abcdabcdabcd"), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").  

Note:  
The length of A and B will be between 1 and 10000.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/repeated-string-match)  

Credits To: [leetcode.com](https://leetcode.com/problems/repeated-string-match/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/repeated-string-match
    ## Basic Ideas: Consider lengths of A and B are len_a, len_b
    ##              Let's say a match exists. k = len_b/len_a
    ##              Then we need to repeat A either k times, k+1 times or k+2 times
    ## Complexity: Time O(m+n), Space O(n)
    class Solution:
        def repeatedStringMatch(self, A, B):
            """
            :type A: str
            :type B: str
            :rtype: int
            """
            lenA, lenB = len(A), len(B)
            times = int(lenB/lenA)
            C = A*times
            if B in C: return times
            if B in C+A: return times+1
            if B in C+A+A: return times+2
            return -1