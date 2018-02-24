# Leetcode: Monotone Increasing Digits     :BLOG:Amusing:


---

Monotone Increasing Digits  

---

Similar Problems:  
-   [Remove K Digits](https://brain.dennyzhang.com/remove-k-digits)
-   [Review: Greedy Problems](https://brain.dennyzhang.com/review-greedy)

---

Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.  

(Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)  

Example 1:  

    Input: N = 10
    Output: 9

Example 2:  

    Input: N = 1234
    Output: 1234

Example 3:  

    Input: N = 332
    Output: 299

Note: N is an integer in the range [0, 10^9].  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/monotone-increasing-digits)  

Credits To: [leetcode.com](https://leetcode.com/problems/monotone-increasing-digits/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/monotone-increasing-digits
    ## Basic Ideas: Greedy
    ##
    ##   After checking the changes, we have one key observastion:
    ##   We need to identity one digit. Decrease it by 1, then change the following to 9
    ##
    ##   So we find the longest non-decreasing sequence from left to right.
    ##   Then scan the sequence from right to left. 
    ##   Keep moving to left, if it's duplicate number.
    ##
    ## Complexity: Time O(1), Space O(1)
    ##       For integer, the maxmium length of digits is small.
    class Solution(object):
        def monotoneIncreasingDigits(self, N):
            """
            :type N: int
            :rtype: int
            """
            l = list(str(N))
            length = len(l)
            for i in range(length): l[i] = ord(l[i]) - ord('0')
    
            # get the longest non-decreasing sequence
            index = -1
            for i in range(length-1):
                if l[i] > l[i+1]:
                    index = i
                    break
            if index == -1: return N
    
            j = -1
            # identity which digit to change
            for i in range(index, -1, -1):
                j = i
                if i>0 and l[i] == l[i-1]:
                    continue
                break
    
            # make the change
            l[j] -= 1
            for i in range(j+1, length): l[i] = 9
    
            # get the result
            res = 0
            for i in range(length): res = res*10+l[i]
            return res
    
    s = Solution()
    print(s.monotoneIncreasingDigits(101)) # 99
    print(s.monotoneIncreasingDigits(120)) # 119
    print(s.monotoneIncreasingDigits(332)) # 299
    print(s.monotoneIncreasingDigits(668841)) # 667999
    print(s.monotoneIncreasingDigits(10)) # 9