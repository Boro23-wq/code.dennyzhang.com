# Leetcode: Longest Substring Without Repeating Characters     :BLOG:Medium:


---

Longest Substring Without Repeating Characters  

---

Similar Problems:  
-   [Leetcode: Substring with Concatenation of All Words](https://brain.dennyzhang.com/substring-with-concatenation-of-all-words)
-   [Review: TwoPointers Problems](https://brain.dennyzhang.com/review-twopointer)

---

Given a string, find the length of the longest substring without repeating characters.  

Examples:  

Given "abcabcbb", the answer is "abc", which the length is 3.  

Given "bbbbb", the answer is "b", with the length of 1.  

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/longest-substring-without-repeating-characters)  

Credits To: [leetcode.com](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/longest-substring-without-repeating-characters
    ## Basic Ideas: two pointer: slow and fast
    ##           If duplicate, the fast pointer don't need to turn back.
    ## Complexity Time O(n), Space O(1)
    class Solution(object):
        def lengthOfLongestSubstring(self, s):
            """
            :type s: str
            :rtype: int
            """
            length = len(s)
            if length <= 1: return length
            ch_set = set()
            max_len, slow, fast = 0, 0, 1
            m = {}
            m[s[slow]] = slow
            while fast < length:
                if s[fast] not in m:
                    m[s[fast]] = fast
                    fast += 1
                else:
                    max_len = max(max_len, len(m))
                    next_slow = m[s[fast]] + 1 
                    for k in xrange(slow, next_slow):
                        del m[s[k]]
                    m[s[fast]] = fast
                    slow = next_slow
                    fast += 1
            return max(max_len, len(m))
    
    s = Solution()         
    print s.lengthOfLongestSubstring('ruowzgiooobpple')
    print s.lengthOfLongestSubstring('bbbbb') # 1
    print s.lengthOfLongestSubstring('pwwkew') # 3