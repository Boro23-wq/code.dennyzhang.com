# Leetcode: Shortest Word Distance     :BLOG:Basic:


---

Shortest Word Distance  

---

Similar Problems:  
-   [Shortest Word Distance II](https://code.dennyzhang.com/shortest-word-distance-ii)
-   Tag: [#array](https://code.dennyzhang.com/tag/array)

---

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.  

For example,  
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].  

Given word1 = "coding", word2 = "practice", return 3.  
Given word1 = "makes", word2 = "coding", return 1.  

Note:  
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/shortest-word-distance)  

Credits To: [leetcode.com](https://leetcode.com/problems/shortest-word-distance/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/shortest-word-distance
    
    class Solution(object):
        ## Basic Ideas: One pass
        ## Complexity: Time O(n), Space O(1)
        def shortestDistance(self, words, word1, word2):
            """
            :type words: List[str]
            :type word1: str
            :type word2: str
            :rtype: int
            """
            p1, p2, res = -1, -1, len(words)
            for i in range(len(words)):
                if words[i] in [word1, word2]:
                    if words[i] == word1:
                        p1 = i
                    else:
                        p2 = i
                    if p1 != -1 and p2 != -1:
                        res = min(res, abs(p1-p2))
            return res
    
        ## Basic Ideas: One pass
        ## Complexity: Time O(n), Space O(1)
        def shortestDistance_v1(self, words, word1, word2):
            """
            :type words: List[str]
            :type word1: str
            :type word2: str
            :rtype: int
            """
            length = len(words)
            pre_index, is_word1 = -1, None
            res = length
            for i in range(length):
                if words[i] in [word1, word2]:
                    if (pre_index != -1) and ((words[i] == word1) != is_word1):
                        res = min(res, i-pre_index)
                    pre_index = i
                    is_word1 = True if words[i] == word1 else False
            return res
    
        ## Basic Ideas:
        ##       One array with tuples: 
        ##          element1: 0/1. 0 indicates word1, 1 indicates word2
        ##             0 0 1 0 1 1 0 0
        ##          element2: index of word1 and word2
        ##       One pass with the array:
        ##          If current is the start of new group, do the caculation.
        ##
        ## Complexity: Time O(n), Space O(n)
        def shortestDistance_v2(self, words, word1, word2):
            """
            :type words: List[str]
            :type word1: str
            :type word2: str
            :rtype: int
            """
            l = []
            for i in range(len(words)):
                if words[i] == word1: l.append((0, i))
                if words[i] == word2: l.append((1, i))
    
            res, prev = len(words), None
            for i in range(len(l)):
                if i == 0:
                    prev = l[i]
                    continue
    
                if l[i][0] != prev[0]:
                    res = min(res, l[i][1]-prev[1])
                prev = l[i]
    
            return res