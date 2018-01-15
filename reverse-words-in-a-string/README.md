# Leetcode: Reverse Words in a String     :BLOG:Basic:


---

Reverse Words in a String  

---

Given an input string, reverse the string word by word.  

For example,  
Given s = "the sky is blue",  
return "blue is sky the".  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/reverse-words-in-a-string)  

Credits To: [Leetcode.com](https://leetcode.com/problems/reverse-words-in-a-string/description/)  

Leave me comments, if you know how to solve.  

    class Solution(object):
        def reverseWords(self, s):
            """
            :type s: str
            :rtype: str
            """
            ## Basic Idea:
            ## the sky is blue
            ## eulb si yks eht
            ## blue is sky the
            ## Complexity: Time O(n), Space O(1)
            # reverse
            s = s[::-1]
            res = 
            for item in s.split(" "):
                if item == "":
                    continue
                res.append(item[::-1])
            return ' '.join(res)