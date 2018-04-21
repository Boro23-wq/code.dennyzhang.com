# LintCode: The Biggest Score On The Tree     :BLOG:Medium:


---

The Biggest Score On The Tree  

---

Given a multitree of n nodes, and the node numbered from 0 to n - 1, and the root numbered 0. Each node has a revenue, you can add the revenue of this node when you get to it. Each side has a cost, we will subtract the cost of this side when walking along it. Find the maximum total (total score = total return - total cost) score from the root node to any leaf node.  

Notice  
-   x[i], y[i] represent two nodes on the ith edge, cost[i] represent the cost of ith edge, profit[i] represent the revenue of node

numbered i.  
-   1 <= x[i], y[i] <= 10^5
-   1 <= cost[i], profit[i] <= 100

Example  

    Given x = [0,0,0],y = [1,2,3], cost = [1,1,1], profit = [1,1,2,3],return 3.
    
    Route: 0->3

    Given x = [0,0],y = [1,2], cost =[1,2], profit = [1,2,5],return 4.
    
    Route: 0->2

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/the-biggest-score-on-the-tree)  

Credits To: [lintcode.com](http://www.lintcode.com/en/problem/the-biggest-score-on-the-tree/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/the-biggest-score-on-the-tree
    class MyTree:
        def __init__(self, profit):
            self.profit = profit
            self.children = []
    
    class Solution:
        """
        @param x: The vertex of edge
        @param y: The another vertex of edge
        @param cost: The cost of edge
        @param profit: The profit of vertex
        @return: Return the max score
        """
        def getMaxScore(self, x, y, cost, profit):
            ## Basic Ideas:
            ##
            ##  Is there a loop? Graph, instead of tree
            ##
            ## Complexity:
            import collections
            nodes = []
            d = {}
            for p in profit: nodes.append(MyTree(p))
    
            for i in range(len(x)):
                nodes[x[i]].children.append(y[i])
                d[(x[i], y[i])] = cost[i]
            queue = collections.deque()
            queue.append((0, nodes[0].profit))
            max_profit = -1
            while len(queue) != 0:
                for k in range(len(queue)):
                    (i, profit) = queue.popleft()
                    if len(nodes[i].children) == 0:
                        max_profit = max(max_profit, profit)
                    else:
                        for j in nodes[i].children:
                            queue.append((j, profit+nodes[j].profit-d[(i, j)]))
            return max_profit