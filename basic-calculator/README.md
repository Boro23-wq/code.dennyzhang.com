# Leetcode: Basic Calculator     :BLOG:Medium:


---

Basic Calculator  

---

Similar Problems:  
-   Tag: [stack](https://brain.dennyzhang.com/tag/stack)

---

Implement a stack calculator to evaluate a simple expression string.  

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .  

You may assume that the given expression is always valid.  

Some examples:  

    "1 + 1" = 2
    " 2-1 + 2 " = 3
    "(1+(4+5+2)-3)+(6+8)" = 23
    Note: Do not use the eval built-in library function.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/basic-calculator)  

Credits To: [leetcode.com](https://leetcode.com/problems/basic-calculator/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/basic-calculator
    ## Basic Ideas: stack
    ##        Whenever we get ), we get the result for (...)
    ##
    ##        # a - b - c != a - (b-c)
    ##
    ## Complexity: Time O(n), Space O(n)
    class Solution(object):
        def calculate(self, s):
            """
            :type s: str
            :rtype: int
            """
            s = s.replace(' ', '')
            length = len(s)
    
            if length == 0: return None
    
            stack = []
            # we can't rely on iterator
            i = 0
            while i < length:
                if s[i] in ['(', '-', '+']:
                    stack.append(s[i])
                elif s[i] == ')':
                    # recursive removal
                    l = []
                    while len(stack) != 0 and stack[-1] != '(':
                        l.insert(0, stack.pop())
                    stack.pop()
                    stack.append(self.calculateList(l))
                else:
                    # digit: get longest token for the number
                    num_str = ''
                    while i < length:
                        if s[i].isdigit() is False: break
                        num_str = '%s%s' % (num_str, s[i])
                        i += 1
                    stack.append(num_str)
                    continue
                i = i + 1
            # we might get expression without parentheses: 1+3+2
            return self.calculateList(stack)
    
        def calculateList(self, l):
            # calculate: 2-3+5-7
            res, i = 0, 0
            while i < len(l):
                element = l[i]
                if element in ['-', '+']:
                    num2 = int(l[i+1])
                    i += 2
                    if element == '-':
                        res -= num2
                    else:
                        res += num2
                else:
                    res += int(element)
                    i += 1
            return res
    s = Solution()
    print s.calculate("(1+(4+5+2)-3)+(6+8)") # 23