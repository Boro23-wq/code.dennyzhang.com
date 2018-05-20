# LintCode: Fermat Point Of Graphs     :BLOG:Medium:


---

Fermat Point Of Graphs  

---

Similar Problems:  
-   [Sum of Distances in Tree](https://code.dennyzhang.com/sum-of-distances-in-tree)
-   Tag: [#classic](https://code.dennyzhang.com/tag/classic), [#dfs](https://code.dennyzhang.com/tag/dfs), [#hashmap](https://code.dennyzhang.com/tag/hashmap)

---

There is a non acyclic connected graph. Each edge is described by two vertices x[i] and y[i], and the length of each edge is described by d[i].  
Find a point p such that the sum of distances from point p to other points is the smallest. If there is more than one such point p, return the smallest number.  

Notice  
-   2 <= n, d[i] <= 10^5
-   1 <= x[i], y[i] <= n

Example  

    Given x = [1], y = [2], d = [3], return 1.
    
    Explanation:
    The distance from other points to 1 is 3, the distance from other points to 2 is 3, and the number of 1 is smaller.

    Given x = [1,2,2], y = [2,3,4], d = [1,1,1], return 2.
    
    Explanation:
    The distance from other points to 1 is 5, the distance from other points to 2 is 3, the distance from other points to 3 is 5, and the distance from other points to 4 is 5.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/fermat-point-of-graphs)  

Credits To: [lintcode.com](https://www.lintcode.com/en/old/problem/fermat-point-of-graphs/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/fermat-point-of-graphs
    import "strconv"
    var edges map[int][]int
    var edge_distances map[string]int
    
    var total_distances []int
    var child_count []int
    var N int
    
    func dfsCount(node int, parent int, distance int) int {
        count := 1
        total_distances[0] += distance
        for _, node2 := range edges[node] {
            if node2!=parent {
                edge := ""
                if node<node2 {
                    edge = strconv.Itoa(node)+":"+strconv.Itoa(node2)
                } else {
                    edge = strconv.Itoa(node2)+":"+strconv.Itoa(node)
                }
                count += dfsCount(node2, node, distance + edge_distances[edge])
            }
        }
        child_count[node] = count
        return count
    }
    
    func dfsDistance(node int, parent int) {
        for _, node2 := range edges[node] {
            if node2!=parent {
                edge := ""
                if node<node2 {
                    edge = strconv.Itoa(node)+":"+strconv.Itoa(node2)
                } else {
                    edge = strconv.Itoa(node2)+":"+strconv.Itoa(node)
                }
                total_distances[node2] = total_distances[node] + (N-2*child_count[node2])*edge_distances[edge]
                dfsDistance(node2, node)
            }
        }
    }
    
    func getFermatPoint (x []int, y []int, d []int) int {
        if len(x) == 0 { return 0 }
        N = len(x)+1
        edge_distances = map[string]int{}
        edges = map[int][]int{}
        for i, node1 := range x {
            node2 := y[i]
            node1, node2 = node1-1, node2-1
            edge := ""
            if node1<node2 {
                edge = strconv.Itoa(node1)+":"+strconv.Itoa(node2)
            } else {
                edge = strconv.Itoa(node2)+":"+strconv.Itoa(node1)
            }
            edge_distances[edge] = d[i]
            edges[node1] = append(edges[node1], node2)
            edges[node2] = append(edges[node2], node1)
        }
        child_count = make([]int, N)
        total_distances = make([]int, N)
        dfsCount(0, -1, 0)
        dfsDistance(0, -1)
        res := 0
        for i:= 1; i< N; i++ {
            if total_distances[i]<total_distances[res] {
                res = i
            }
        }
        return res+1
    }