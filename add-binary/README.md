# Leetcode: Add Binary     :BLOG:Basic:


---

Given two binary strings, return their sum  

---

Given two binary strings, return their sum (also a binary string).  

For example,  
a = "11"  
b = "1"  
Return "100".  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/add-binary)  

Credits To: [leetcode.com](https://leetcode.com/problems/add-binary/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/add-binary
    class Solution(object):
        def addBinary(self, a, b):
            """
            :type a: str
            :type b: str
            :rtype: str
            """
            val1 = 0
            for ch in a:
                val1 = val1 << 1
                if ch == '1':
                    val1 = val1 + 1
                else:
                    if ch != '0':
                        raise Exception("Invalid output")
    
            val2 = 0
            for ch in b:
                val2 = val2 << 1
                if ch == '1':
                    val2 = val2 + 1
                else:
                    if ch != '0':
                        raise Exception("Invalid output")
    
            # print("val1: %s, val2: %s" % (val1, val2))
            l = []
            val = val1 + val2
            if val == 0:
                return "0"
            else:
                while val != 0:
                    l.append(str(val % 2))
                    val = val >> 1
                l.reverse()
                return "".join(l)