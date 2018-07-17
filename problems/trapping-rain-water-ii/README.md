# Leetcode: Trapping Rain Water II     :BLOG:Hard:


---

Trapping Rain Water II  

---

Similar Problems:  
-   [Trapping Rain Water](https://code.dennyzhang.com/container-water)
-   [Minimum Height Trees](https://code.dennyzhang.com/minimum-height-trees)
-   Tag: [#trappingrain](https://code.dennyzhang.com/tag/trappingrain), [#bfs](https://code.dennyzhang.com/tag/bfs), [#heap](https://code.dennyzhang.com/tag/heap), [#outer2inside](https://code.dennyzhang.com/tag/outer2inside), [#inspiring](https://code.dennyzhang.com/tag/inspiring)

---

Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.  

Note:  
Both m and n are less than 110. The height of each unit cell is greater than 0 and is less than 20,000.  

Example:  

    Given the following 3x6 height map:
    [
      [1,4,3,1,3,2],
      [3,2,1,3,2,4],
      [2,3,3,2,3,1]
    ]
    
    Return 4.

![img](//raw.githubusercontent.com/DennyZhang/challenges-leetcode-interesting/master/images/rainwater_empty.png)  

The above image represents the elevation map [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain.  
![img](//raw.githubusercontent.com/DennyZhang/challenges-leetcode-interesting/master/images/rainwater_fill.png)  

After the rain, water is trapped between the blocks. The total volume of water trapped is 4.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/trapping-rain-water-ii)  

Credits To: [leetcode.com](https://leetcode.com/problems/trapping-rain-water-ii/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution: XXX

**General Thinkings:**  


**Key Observations:**  


**Walk Through Testdata**  


    // Blog link: https://code.dennyzhang.com/trapping-rain-water-ii
    // Basic Ideas: heap
    // The lowest bucket determine how much water it can hold.
    //
    // Start from the outer circle into the inner circles
    // We explore from the lowest blocks(use min-heap)
    // If unexamined bucket is small then current lowest, current bucket can hold some water
    // Otherwise current bucket can't hold water
    //
    // Complexity: Time ?, Space ?
    import "container/heap"
    // https://golang.org/pkg/container/heap/
    
    type Item struct {
      x, y, v int
    }
    
    // A PriorityQueue implements heap.Interface and holds Items.
    type PriorityQueue []*Item
    
    func (pq PriorityQueue) Len() int { return len(pq) }
    
    func (pq PriorityQueue) Less(i, j int) bool {
            // We want Pop to give us the highest, not lowest, priority so we use greater than here.
            return pq[i].v < pq[j].v
    }
    
    func (pq PriorityQueue) Swap(i, j int) {
            pq[i], pq[j] = pq[j], pq[i]
    }
    
    func (pq *PriorityQueue) Push(x interface{}) {
            item := x.(*Item)
            *pq = append(*pq, item)
    }
    
    func (pq *PriorityQueue) Pop() interface{} {
            old := *pq
            n := len(old)
            item := old[n-1]
            *pq = old[0 : n-1]
            return item
    }
    
    func trapRainWater(heightMap [][]int) int {
        if len(heightMap) == 0 { return 0 }
    
        visited := map[string]bool{}
        h := make(PriorityQueue, 0)
            heap.Init(&h)
        // add outer bounders to min-heap
        for _, i := range []int{0, len(heightMap)-1} {
            for j := 0; j < len(heightMap[0]); j++ {
                heap.Push(&h, &Item{i, j, heightMap[i][j]})
                visited[fmt.Sprintf("%d-%d", i, j)] = true
            }
        }
        for i:=1; i<len(heightMap)-1; i++ {
            for _, j:= range []int{0, len(heightMap[0])-1} {
                heap.Push(&h, &Item{i, j, heightMap[i][j]})
                visited[fmt.Sprintf("%d-%d", i, j)] = true
            }
        }
    
        res := 0
        x, y := 0, 0
        key := ""
        for h.Len() != 0 {
            item := heap.Pop(&h).(*Item)
            // fmt.Println("item: ", item)
            for _, offset := range [][]int{[]int{0, 1}, []int{0, -1}, []int{1, 0}, []int{-1, 0}} {
                x, y = item.x+offset[0], item.y+offset[1]
                if x<0 || x>=len(heightMap) || y<0 || y>=len(heightMap[0]) {
                    continue
                }
                key = fmt.Sprintf("%d-%d", x, y)
                if visited[key] { continue }
                visited[key] = true
                if heightMap[x][y] < item.v {
                    // fmt.Println(item.x, item.y, item.v, "|", x, y, item.v - heightMap[x][y])
                    res += item.v - heightMap[x][y]
                    heap.Push(&h, &Item{x, y, item.v})
                } else {
                    heap.Push(&h, &Item{x, y, heightMap[x][y]})
                }                                
            }
        }
        return res
    }