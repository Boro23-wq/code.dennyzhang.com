# Leetcode: Maximum Product of Word Lengths     :BLOG:Medium:


---

Maximum Product of Word Lengths  

---

Given a string array words, find the maximum value of length(word[i]) \* length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.  

    Example 1:
    Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
    Return 16
    The two words can be "abcw", "xtfn".

    Example 2:
    Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
    Return 4
    The two words can be "ab", "cd".

    Example 3:
    Given ["a", "aa", "aaa", "aaaa"]
    Return 0
    No such pair of words.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/maximum-product-of-word-lengths)  

Credits To: [leetcode.com](https://leetcode.com/problems/maximum-product-of-word-lengths/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: http://brain.dennyzhang.com/maximum-product-of-word-lengths
    ## Basic Ideas: Convert each word into 26 bits binary.
    ##              b[0] -> a, b[1] -> b, b[2] -> c ... b[25] -> z
    ##              If b1 & b2 == 0, no common letters between word1 and word2
    ##
    ## Complexity: Time O(n*n), Space O(n)
    class Solution(object):
        def maxProduct(self, words):
            """
            :type words: List[str]
            :rtype: int
            """
            length = len(words)
            binary_list = [0] * length
            mask_dict = {}
            num = 1
            for ascii in range(ord('a'), ord('z') + 1):
                mask_dict[chr(ascii)] = num
                num = num << 1
    
            # Convert each word to binary
            for i in xrange(length):
                binary = 0
                for ch in words[i]:
                    binary = binary | mask_dict[ch]
                binary_list[i] = binary
    
            max_product = 0
            for i in xrange(length-1):
                for j in range(i+1, length):
                    if binary_list[i] & binary_list[j] == 0:
                        product = len(words[i]) * len(words[j])
                        max_product = max(max_product, product)
            return max_product
    
    s = Solution()
    print s.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]) # 16
    print s.maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]) # 4
    print s.maxProduct(["a", "aa", "aaa", "aaaa"]) # 0