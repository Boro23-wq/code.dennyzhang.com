# Leetcode: Minimum Window Substring     :BLOG:Hard:


---

Minimum Window Substring  

---

Similar Problems:  
-   [Substring with Concatenation of All Words](https://brain.dennyzhang.com/substring-with-concatenation-of-all-words)
-   Tag: [#twopointer](https://brain.dennyzhang.comy/tag/twopointer)

---

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).  

    For example,
    S = "ADOBECODEBANC"
    T = "ABC"
    Minimum window is "BANC".

Note:  
If there is no such window in S that covers all characters in T, return the empty string "".  

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/minimum-window-substring)  

Credits To: [leetcode.com](https://leetcode.com/problems/minimum-window-substring/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/minimum-window-substring
    ## Basic Ideas: two pointer
    ##              Find all candidates, and get the mininum window
    ##
    ## Complexity: Time O(n), Space O(1)
    import collections
    class Solution:
        def minWindow(self, s, t):
            """
            :type s: str
            :type t: str
            :rtype: str
            """
            len1, len2 = len(s), len(t)
            if len2>len1: return ""
            if len1 == 0: return ""
            m1 = collections.defaultdict(lambda:0)
            m2 = collections.defaultdict(lambda:0)
            for i in range(0, len2): m2[t[i]] += 1
    
            min_len, res = sys.maxsize, ""
            left, right = 0, 0
            for right in range(0, len1):
                m1[s[right]] += 1
                if self.isTooSmall(m1, m2): continue
                # find a match, then check whether window too big
                while m1[s[left]] > m2[s[left]]:
                    m1[s[left]] -= 1
                    left += 1
                # find a candidate
                if min_len > right-left+1:
                    min_len, res = right-left+1, s[left:right+1]
            return res
    
        def isTooSmall(self, m1, m2):
            for ch in m2:
                if m1[ch] < m2[ch]: return True
            return False
    
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC")) # BANC