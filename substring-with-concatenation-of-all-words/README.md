# Leetcode: Substring with Concatenation of All Words     :BLOG:Hard:


---

Substring with Concatenation of All Words  

---

Similar Problems:  
-   [Longest Substring Without Repeating Characters](https://code.dennyzhang.com/longest-substring-without-repeating-characters)
-   [Minimum Window Substring](https://code.dennyzhang.com/minimum-window-substring)
-   Tag: [#twopointer](https://code.dennyzhang.comy/tag/twopointer)

---

You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.  

    For example, given:
    s: "barfoothefoobarman"
    words: ["foo", "bar"]
    
    You should return the indices: [0,9].
    (order does not matter).

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/substring-with-concatenation-of-all-words)  

Credits To: [leetcode.com](https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/substring-with-concatenation-of-all-words
    ## Basic Ideas: 2 twopointers with hasmap
    ##
    ##  Assumption: no duplicate word in words. 
    ##              len(s) % len(words[0]) == 0
    ##
    ## Complexity: Time O(n*k), Space O(m). k=len(words[0]), m=len(words)*len(words[0])
    import collections
    class Solution:
        def findSubstring(self, s, words):
            """
            :type s: str
            :type words: List[str]
            :rtype: List[int]
            """
            len_s = len(s)
            if len(words) == 0 or words == [""]:
                return range(0, len_s)
    
            if len_s < len(words)*len(words[0]): return []
            len_word = len(words[0])
    
            m1 = collections.defaultdict(lambda: 0)
            m2 = collections.defaultdict(lambda: 0)
            for word in words: m2[word] += 1
            res = []
            left, right = 0, 0
            for right in range(0, int(len_s/len_word)):
                right_word = s[right*len_word:(right+1)*len_word]
                m1[right_word] += 1
                # not long enough for sliding window
                if (right+1)*len_word < len(words)*len(words[0]): continue
    
                if m1 == m2: res.append(left*len_word)
                left_word = s[left*len_word:(left+1)*len_word]
                m1[left_word] -= 1
                if m1[left_word] == 0: del m1[left_word]
                left += 1
            return res
    
    # s = Solution()
    # print(s.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"])) # [6, 9, 12]