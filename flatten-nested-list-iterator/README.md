# Leetcode: Flatten Nested List Iterator     :BLOG:Hard:


---

Flatten Nested List Iterator  

---

Given a nested list of integers, implement an iterator to flatten it.  

Each element is either an integer, or a list &#x2013; whose elements may also be integers or other lists.  

    Example 1:
    Given the list [[1,1],2,[1,1]],
    
    By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

    Example 2:
    Given the list [1,[4,[6]]],
    
    By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/flatten-nested-list-iterator)  

Credits To: [leetcode.com](https://leetcode.com/problems/flatten-nested-list-iterator/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: http://brain.dennyzhang.com/flatten-nested-list-iterator
    ## Basic Ideas:
    ##            Since it's an iterator, we can't change existing list
    ##            Here we assume, we don't have empty values like this: [1, 2, [], [2, 3]]
    ##
    ##            l1: list of original input
    ##            index: index of original list
    ##            l2: list to cache the embeded data
    ##
    ##            next:
    ##               If l2 is empty, get one element from l1. And move index to next
    ##                  If the element is an integer, return
    ##                  If not, get the very first element. And insert the rest to l2
    ##                       Watch out: [[[[1, 2], [3], 4], 5], 6]
    ##               If l2 is not empty, do the same like above
    ##
    ##             has_next:
    ##                If l2 is not empty, return False
    ##                Otherwise return index != len(l1)
    ##
    ## Complexity:
    # """
    # This is the interface that allows for creating nested lists.
    # You should not implement it, or speculate about its implementation
    # """
    #class NestedInteger(object):
    #    def isInteger(self):
    #        """
    #        @return True if this NestedInteger holds a single integer, rather than a nested list.
    #        :rtype bool
    #        """
    #
    #    def getInteger(self):
    #        """
    #        @return the single integer that this NestedInteger holds, if it holds a single integer
    #        Return None if this NestedInteger holds a nested list
    #        :rtype int
    #        """
    #
    #    def getList(self):
    #        """
    #        @return the nested list that this NestedInteger holds, if it holds a nested list
    #        Return None if this NestedInteger holds a single integer
    #        :rtype List[NestedInteger]
    #        """
    
    import copy
    class NestedIterator(object):
    
        def __init__(self, nestedList):
            """
            Initialize your data structure here.
            :type nestedList: List[NestedInteger]
            """
            self.l1 = nestedList
            self.index = 0
            self.l2 = []
    
        def next(self):
            """
            :rtype: int
            """
            if len(self.l2) != 0:
                node = self.l2[0]
                del self.l2[0]
                (first, rest) = self.getFirst(node)
                if rest: self.l2.insert(0, rest)
            else:
                node = self.l1[self.index]
                self.index += 1
                (first, rest) = self.getFirst(node)
                if rest: self.l2.append(rest)
            return first
    
        def getFirst(self, node):
            p = copy.deepcopy(node)
    
            q, parent_list = p, []
            while True:
                # q may be: list or NestedInteger
                if type(q) == list:
                    parent_list.append(q)
                    q = q[0]
                elif q.isInteger():
                    break
                else:
                    item = q.getList()
                    parent_list.append(item)
                    q = item[0]
    
            first_val = q.getInteger()
            if len(parent_list) != 0:
                del parent_list[-1][0]
    
            # delete empty element at the head
            for i in range(len(parent_list)-1, -1, -1):
                l = parent_list[i]
                if len(l) != 0 and l[0] == []:
                    del l[0]
    
            if len(parent_list) != 0:
                rest = parent_list[0]
                # change [item] to item
                if len(rest) == 1:
                    return (first_val, rest[0])
                else:
                    return (first_val, rest)
            else:
                return (first_val, None)
    
        def hasNext(self):
            """
            :rtype: bool
            """
            if len(self.l2) == 0 and self.index == len(self.l1):
                return False
            else:
                return True
    
    # Your NestedIterator object will be instantiated and called as such:
    # i, v = NestedIterator(nestedList), []
    # while i.hasNext(): v.append(i.next())

---

Similar Problems:  
-   [Leetcode: Mini Parser](http://brain.dennyzhang.com/mini-parser)
-   [Review: Stack Problems](http://brain.dennyzhang.com/review-stack)