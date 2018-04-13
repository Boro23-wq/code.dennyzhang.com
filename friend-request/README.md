# LintCode: Friend Request     :BLOG:Basic:


---

Friend Request  

---

Similar Problems:  
-   [Tag: #array](https://code.dennyzhang.com/tag/array)

---

Given an array Ages of length n, where the first i elements represent the age of the individual i Find total number of friend requests sent by this n person. There are some requirements:  
1.  if Age(B) <= (1/2)Age(A) + 7, A will not send a request to B.
2.  if Age(B) > Age(A), A will not send a request to B.
3.  if Age(B) < 100 and Age(A) > 100, A will not send a request to B.
4.  If it does not satisfy 1,2,3, then A will send a request to B

Notice  
-   Ages.length <= 1000
-   Everyone's age is greater than 0, less than 150

Example  
Given Ages = [10,39,50], return 1.  

    Explanation:
    Only people of age 50 will send friend requests to people of age 39.

Given Ages = [101,79,102], return 1.  

    Explanation:
    Only people of age 102 will send friend requests to people of age 101.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/friend-request)  

Credits To: [lintcode.com](http://www.lintcode.com/en/problem/friend-request/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/friend-request
    ## Basic Ideas: two loop
    ## Complexity: Time O(n*n), Space O(1)
    class Solution:
        """
        @param ages: The ages
        @return: The answer
        """
        def friendRequest(self, ages):
            res = 0
            for i in range(len(ages)):
                for j in range(len(ages)):
                    if i == j: continue
                    if ages[j]<=(1/2)*ages[i]+7: continue
                    if ages[j]>ages[i]: continue
                    if ages[j]<100 and ages[i]>100: continue
                    res += 1
            return res