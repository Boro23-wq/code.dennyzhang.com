# Leetcode: Sum of Distances in Tree     :BLOG:Hard:


---

Sum of Distances in Tree  

---

Similar Problems:  
-   Tag: [#classic](https://code.dennyzhang.com/tag/classic), [#dfs](https://code.dennyzhang.com/tag/dfs), [#hashmap](https://code.dennyzhang.com/tag/hashmap)

---

An undirected, connected tree with N nodes labelled 0&#x2026;N-1 and N-1 edges are given.  

    The ith edge connects nodes edges[i][0] and edges[i][1] together.

Return a list ans, where ans[i] is the sum of the distances between node i and all other nodes.  

Example 1:  

    Input: N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
    Output: [8,12,6,10,10,10]
    Explanation: 
    Here is a diagram of the given tree:
      0
     / \
    1   2
       /|\
      3 4 5
    We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
    equals 1 + 1 + 2 + 2 + 2 = 8.  Hence, answer[0] = 8, and so on.

Note: 1 <= N <= 10000  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/sum-of-distances-in-tree)  

Credits To: [leetcode.com](https://leetcode.com/problems/sum-of-distances-in-tree/description/)  

Leave me comments, if you have better ways to solve.  

    // Blog link: https://code.dennyzhang.com/sum-of-distances-in-tree
    // When we move our root from one node to its connected node, 
    //  one part of nodes get closer, one the other part get further.
    // Basic Ideas: dfs, hashmap
    // Complexity: Time O(n) Space O(n)
    var m_edges map[int][]int
    
    // No need to use hashmap here
    var m_childcnt []int
    var m_distances []int
    
    func dfsCnt(node int, parent int, distance int) int {
        m_distances[0] += distance
        res := 1
        for _, child := range m_edges[node] {
            if child != parent {
                res += dfsCnt(child, node, distance+1)
            }
        }
        m_childcnt[node] = res
        return res
    }
    
    func dfsDistance(node int, parent int, N int) {
        if parent != -1 {
            m_distances[node] = m_distances[parent] + N - 2*m_childcnt[node]
        }
        for _, child := range m_edges[node] {
            if parent != child { dfsDistance(child, node, N) }
        }
    }
    
    func sumOfDistancesInTree(N int, edges [][]int) []int {
        m_edges = map[int][]int{}
        for i, _ := range edges {
            edge := edges[i]
            m_edges[edge[0]] = append(m_edges[edge[0]], edge[1])
            m_edges[edge[1]] = append(m_edges[edge[1]], edge[0])
        }
        m_childcnt = make([]int, N)
        m_distances = make([]int, N)
        m_distances[0] = 0
        dfsCnt(0, 0, 0)
        dfsDistance(0, -1, N)
        return m_distances
    }