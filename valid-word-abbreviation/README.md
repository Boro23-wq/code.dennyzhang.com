# Leetcode: Valid Word Abbreviation     :BLOG:Basic:


---

Valid Word Abbreviation  

---

Similar Problems:  
-   [Flip Game](https://brain.dennyzhang.com/flip-game)
-   [Tag: #string](https://brain.dennyzhang.com/tag/string)
-   [Tag: #classic](https://brain.dennyzhang.com/tag/classic)

---

Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.  

A string such as "word" contains only the following valid abbreviations:  

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]  
Notice that only the above abbreviations are valid abbreviations of the string "word". Any other string is not a valid abbreviation of "word".  

Note:  
Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.  

Example 1:  

    Given s = "internationalization", abbr = "i12iz4n":
    
    Return true.

Example 2:  

    Given s = "apple", abbr = "a2e":
    
    Return false.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/valid-word-abbreviation)  

Credits To: [leetcode.com](https://leetcode.com/problems/valid-word-abbreviation/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/valid-word-abbreviation
    ## Basic Ideas: two pointer
    ## Complexity: Time O(n), Space O(1)
    class Solution:
        def validWordAbbreviation(self, word, abbr):
            """
            :type word: str
            :type abbr: str
            :rtype: bool
            """
            j, count = 0, 0
            for i in range(len(word)):
                if count != 0:
                    count -= 1
                    continue
                # abbr is shorter
                if j >= len(abbr): return False
                if abbr[j].isalpha():
                    if abbr[j] != word[i]: return False
                    j += 1
                else:
                    # invalid number
                    if abbr[j] == '0': return False
                    # find number
                    end_index = j
                    for k in range(j+1, len(abbr)):
                        if abbr[k].isdigit():
                            end_index = k
                        else:
                            break
                    count = int(abbr[j:end_index+1])
                    j = end_index+1
                    # match current character
                    count -= 1
            # check whether abbr is longer
            return count == 0 and j == len(abbr)