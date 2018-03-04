# Leetcode: Excel Sheet Column Title     :BLOG:Medium:


---

Excel Sheet Column Title  

---

Given a positive integer, return its corresponding column title as appear in an Excel sheet.  

    For example:
    
        1 -> A
        2 -> B
        3 -> C
        ...
        26 -> Z
        27 -> AA
        28 -> AB

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/excel-sheet-column-title)  

Credits To: [leetcode.com](https://leetcode.com/problems/excel-sheet-column-title/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/excel-sheet-column-title
    ## Basic Ideas:
    ##         a*(26^3) + b*(26^2) + c*(26) + d
    ##          1 ->  (1)  -> A
    ##          25 -> (25) -> Y
    ##          26 -> (10) -> Z
    ##          27 -> (11) -> AA
    ##          28 -> (12) -> AB
    ##       2*26+0 -> (20) ->  AZ
    ## Complexity:
    class Solution(object):
        def convertToTitle(self, n):
            """
            :type n: int
            :rtype: str
            """
            res = ""
            while n != 0:
                mod_val = n % 26
                n = n/26
                if mod_val == 0:
                    ch = 'Z'
                    n = n-1
                else:
                    ch = self.numberToCharacter(mod_val)
                res = "%s%s" % (ch, res)
            return res
    
        def numberToCharacter(self, n):
            if n<1 or n >26:
                raise Exception("Unexpected input")
            return chr(ord('A') + (n-1))
    
    # s = Solution()
    # print s.convertToTitle(26) #Z
    # print s.convertToTitle(27) #AA
    # print s.convertToTitle(2) #B
    # print s.convertToTitle(52) #AZ