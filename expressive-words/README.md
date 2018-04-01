# Leetcode: Expressive Words     :BLOG:Medium:


---

Expressive Words  

---

Similar Problems:  
-   Tag: [#string](https://brain.dennyzhang.com/tag/string)

---

Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  Here, we have groups, of adjacent letters that are all the same character, and adjacent characters to the group are different.  A group is extended if that group is length 3 or more, so "e" and "o" would be extended in the first example, and "i" would be extended in the second example.  As another example, the groups of "abbcccaaaa" would be "a", "bb", "ccc", and "aaaa"; and "ccc" and "aaaa" are the extended groups of that string.  

For some given string S, a query word is stretchy if it can be made to be equal to S by extending some groups.  Formally, we are allowed to repeatedly choose a group (as defined above) of characters c, and add some number of the same character c to it so that the length of the group is 3 or more.  Note that we cannot extend a group of size one like "h" to a group of size two like "hh" - all extensions must leave the group extended - ie., at least 3 characters long.  

Given a list of query words, return the number of words that are stretchy.  

Example:  

    Input: 
    S = "heeellooo"
    words = ["hello", "hi", "helo"]
    Output: 1
    Explanation: 
    We can extend "e" and "o" in the word "hello" to get "heeellooo".
    We can't extend "helo" to get "heeellooo" because the group "ll" is not extended.

Notes:  

-   0 <= len(S) <= 100.
-   0 <= len(words) <= 100.
-   0 <= len(words[i]) <= 100.
-   S and all words in words consist only of lowercase letters

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/expressive-words)  

Credits To: [leetcode.com](https://leetcode.com/problems/expressive-words/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/expressive-words
    ## Basic Ideas:
    ##    From "heeellooo To": ["h", "3", "e", "l", "l", "3", "o"]
    ##    Then compare it with ["hello", "hi", "helo"]
    ## Complexity:
    class Solution:
        def expressiveWords(self, S, words):
            """
            :type S: str
            :type words: List[str]
            :rtype: int
            """
            l = []
            i = 0
            while i < len(S):
                if i+2 < len(S) and S[i:i+3] == S[i]*3:
                    index = len(S)
                    for j in range(i+3, len(S)):
                        if S[j] != S[j-1]:
                            index = j
                            break
                    l.append(str(index-i))
                    l.append(S[i])
                    i = index
                else:
                    l.append(S[i])
                    i += 1
    
            res = 0
            for word in words:
                i, j = 0, 0
                while i<len(l) and j < len(word):
                    if l[i].isdigit():
                        count = int(l[i])
                        i += 1
                        if l[i] != word[j]: break
                        # find occurence in word
                        while j<len(word) and word[j] == l[i]:
                            j, count = j+1, count-1
                        # no enough occurence in string S
                        if count < 0: break
                        i += 1
                    else:
                        if l[i] != word[j]: break
                        i, j = i+1, j+1
    
                if i == len(l) and j == len(word):
                    res += 1
    
            return res