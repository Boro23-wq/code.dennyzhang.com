# Leetcode: Happy Number     :BLOG:Hard:


---

Happy Number  

---

Write an algorithm to determine if a number is "happy".  

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.  

    Example: 19 is a happy number
    
    12 + 92 = 82
    82 + 22 = 68
    62 + 82 = 100
    12 + 02 + 02 = 1

Blog link: <http://brain.dennyzhang.com/happy-number>  

Github: challenges-leetcode-interesting  

Credits To: leetcode.com  

Leave me comments, if you know how to solve.  

    ## Basic Ideas: Floyd Cycle
    ##
    ## Complexity: Time O(n), Space O(1)
    class Solution(object):
        def isHappy(self, n):
            """
            :type n: int
            :rtype: bool
            """
            slow, fast = n, n
            while True:
                slow = self.getCaculatedSum(slow)
                fast = self.getCaculatedSum(self.getCaculatedSum(fast))
                if slow == fast: break
            return True if slow == 1 else False
    
        def getCaculatedSum(self, n):
            if n < 0:
                return None
            if n == 0:
                return 0
            res = 0
            while n != 0:
                ldigit = n % 10
                res = res + ldigit*ldigit
                n = n/10
            return res