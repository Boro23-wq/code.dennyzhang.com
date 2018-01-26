# Leetcode: Top K Frequent Elements     :BLOG:Basic:


---

Top K Frequent Elements  

---

Similar Problems:  
-   Tag: [#topk](http://brain.dennyzhang.com/tag/topk)

---

Given a non-empty array of integers, return the k most frequent elements.  

For example,  
Given [1,1,1,2,2,3] and k = 2, return [1,2].  

Note:  
You may assume k is always valid, 1 <= k <= number of unique elements.  
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/top-k-frequent-elements)  

Credits To: [leetcode.com](https://leetcode.com/problems/top-k-frequent-elements/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: http://brain.dennyzhang.com/top-k-frequent-elements
    ## Basic Ideas: priority queue: heapq
    ##
    ## Complexity:
    import collections, heapq
    class Solution(object):
        def topKFrequent(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: List[int]
            """
            q = 
            heapq._heapify_max(q)
            m = collections.defaultdict(lambda: 0)
            for num in nums: m[num] += 1
            # python heapq doesn't support max heap by default
            for num in m: heapq.heappush(q, (-m[num], num))
    
            res = 
            for i in xrange(k):
                (count, num) = heapq.heappop(q)
                res.append(num)
            return res