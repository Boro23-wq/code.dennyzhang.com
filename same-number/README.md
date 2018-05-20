# Lintcode: Same Number     :BLOG:Basic:


---

Same Number  

---

Similar Problems:  
-   Tag: [#hashmap](https://code.dennyzhang.com/tag/hashmap)

---

Given an array, If the same number exists in the array, and the distance of the same number is less than the given value k, output YES, otherwise output NO.  

Notice  
-   The length of the given array is n, and n <= 100000.
-   The element is x, 0 <= x <= 1e9.
-   1 <= k < n

Example  

    Given array = [1,2,3,1,5,9,3], k = 4, return "YES".
    
    Explanation:
    
    The distance of 1 whose indexes are  3 and 0 is 3, which meets the requirement and output YES.

    Given array =[1,2,3,5,7,1,5,1,3], k = 4, return "YES".
    
    Explanation:
    The distance of 1 whose indexes are  7 and 5 is 2, which meets the requirement and output YES.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/same-number)  

Credits To: [lintcode.com](http://www.lintcode.com/en/problem/same-number/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/same-number
    class Solution:
        """
        @param nums: the arrays
        @param k: the distance of the same number
        @return: the ans of this question
        """
        def sameNumber(self, nums, k):
            ## Basic Ideas: hashmap
            ## Complexity: Time O(n), Space O(n)
            import collections
            m = collections.defaultdict(lambda: [])
            for i, num in enumerate(nums):
                m[num].append(i)
    
            for num in m:
                l = m[num]
                if len(l) > 1:
                    # print(num, l)
                    for i in range(len(l)-1):
                        if l[i+1] - l[i] < k:
                            return "YES"
            return "NO"