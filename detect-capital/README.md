# Leetcode: Detect Capital     :BLOG:Basic:


---

Given a word, you need to judge whether the usage of capitals in it is right or not.  

---

Given a word, you need to judge whether the usage of capitals in it is right or not.  

We define the usage of capitals in a word to be right when one of the following cases holds:  

1.  All letters in this word are capitals, like "USA".
2.  All letters in this word are not capitals, like "leetcode".
3.  Only the first letter in this word is capital if it has more than one letter, like "Google".

Otherwise, we define that this word doesn't use capitals in a right way.  

    Example 1:
    Input: "USA"
    Output: True

    Example 2:
    Input: "FlaG"
    Output: False

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/detect-capital)  

Credits To: [leetcode.com](https://leetcode.com/problems/detect-capital/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/detect-capital
    ## Basic Ideas: Scan once
    ## Complexity: Time O(n), Space O(1)
    class Solution(object):
        def detectCapitalUse(self, word):
            """
            :type word: str
            :rtype: bool
            """
            upper_letters = map(chr, range(ord('A'), ord('Z')+1))
    
            length = len(word)
            upper_count = 0
    
            if length == 0:
                return False
    
            for ch in word:
                if ch in upper_letters:
                    upper_count += 1
    
            if length == 1:
                return True
            else:
                if word[0] in upper_letters:
                    return (upper_count == 1) or (upper_count == length)
                else:
                    return upper_count == 0