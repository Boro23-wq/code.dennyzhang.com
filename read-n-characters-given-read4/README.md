# Leetcode: Read N Characters Given Read4     :BLOG:Basic:


---

Read N Characters Given Read4  

---

Similar Problems:  
-   Tag: [#basic](https://brain.dennyzhang.com/tag/basic)

---

The API: int read4(char \*buf) reads 4 characters at a time from a file.  

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.  

By using the read4 API, implement the function int read(char \*buf, int n) that reads n characters from the file.  

Note:  
The read function will only be called once for each test case.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/read-n-characters-given-read4)  

Credits To: [leetcode.com](https://leetcode.com/problems/read-n-characters-given-read4/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/read-n-characters-given-read4
    ## Basic Ideas: Use cached reading
    ##     Notice: We don't need to save the status of previous read function
    ##
    ## Complexity: Time O(n), Space O(1)
    # The read4 API is already defined for you.
    # @param buf, a list of characters
    # @return an integer
    # def read4(buf):
    
    class Solution(object):
        def read(self, buf, n):
            """
            :type buf: Destination buffer (List[str])
            :type n: Maximum number of characters to read (int)
            :rtype: The number of characters read (int)
            """
            if n <= 0: return 0
            res = 0
            # We deliberately do one possible extra read
            for i in range(0, int(n/4)+1):
                buf_tmp = [' ']*4
                cur = read4(buf_tmp)
                # get the result
                for i in range(0, cur):
                    buf[res+i] = buf_tmp[i]
                res += cur
                # no more to read
                if cur == 0: break
            return min(res, n)