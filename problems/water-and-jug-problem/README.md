
# Leetcode: Water and Jug Problem     :BLOG:Medium:

---

Water and Jug Problem  

---

Similar Problems:  

-   [Reaching Points](https://code.dennyzhang.com/reaching-points)
-   [Max Points on a Line](https://code.dennyzhang.com/max-points-on-a-line)
-   [Review: gcd Problems](https://code.dennyzhang.com/review-gcd)
-   Tag: [#game](https://code.dennyzhang.com/tag/game), [#gcd](https://code.dennyzhang.com/tag/gcd), [#classic](https://code.dennyzhang.com/tag/classic), [#math](https://code.dennyzhang.com/tag/math)

---

You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.  

If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.  

Operations allowed:  

Fill any of the jugs completely with water.  
Empty any of the jugs.  
Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.  
Example 1: (From the famous ["Die Hard"](https://www.youtube.com/watch?v=BVtQNK_ZUJg) example)  

    Input: x = 3, y = 5, z = 4
    Output: True

Example 2:  

    Input: x = 2, y = 6, z = 5
    Output: False

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/water-and-jug-problem)  

Credits To: [leetcode.com](https://leetcode.com/problems/water-and-jug-problem/description/)  

Leave me comments, if you have better ways to solve.  

---

-   GCD

    // Blog link: https://code.dennyzhang.com/water-and-jug-problem
    // Basic Ideas: Math: gcd
    //
    //  Let's say we can make it. It means z=ax+by
    //  Given gcd(a, b)=d. We know (ax+by)%d == 0. So z%d==0
    //
    // Complexity: Time O(1), Space O(1)
    func getGCD(x int, y int) int {
        for y!= 0 {
    	x, y = y, x%y
        }
        return x
    }
    
    func canMeasureWater(x int, y int, z int) bool {
        if z==x || z==y || z==x+y { return true }
        if z>x+y { return false }
        return z%getGCD(x, y) == 0
    }

-   BFS

    // Blog link: https://code.dennyzhang.com/water-and-jug-problem
    // Basic Ideas: BFS
    //
    // (i, j), i is what jug x hold, j is what jug y hold
    //    The next state of (i, j) is
    //          pour jug x to jug y: (0, (i+j)%y)
    //          pour jug y to jug x: ((i+j)%x, 0)
    //          dump jug x: (0, j)
    //          dump jug y: (i, 0)
    //          fill jug x: (x, j)
    //          fill jug y: (i, y)
    //
    // The initial state is (0, 0). 
    // When i+j == z, return true.
    // When all possible combinations have been tried, return false
    //
    // Complexity:
    type Entity struct {
        x, y int
    }
    
    func canMeasureWater(x int, y int, z int) bool {
        if z==x || z==y || z==x+y || z==0 { return true }
        if z>x+y { return false }
        if x==0 { return z==y }
        if y==0 { return z==x }
    
        queue := []Entity{}
        visited := map[Entity]bool{}
    
        i, j := 0, 0
        visited[Entity{i, j}] = true
        queue = append(queue, Entity{i, j})
    
        for len(queue) != 0 {
    	array := []Entity{}
    	for _, item := range queue {
    	    for _, item2 := range [][]int{[]int{0, (item.x+item.y)%y}, 
    		[]int{(item.x+item.y)%x, 0}, []int{0, item.y},
    		[]int{item.x, 0}, []int{x, item.y}, []int{item.x, y}} {
    		    // explore next state
    		    i, j = item2[0], item2[1]
    		    if i+j == z { return true }
    		    item2 := Entity{i, j}
    		    if visited[item2] == false {
    			visited[item2] = true
    			array = append(array, item2)
    		    }
    		}
    	}
    	// copy back to the original queue
    	queue = []Entity{}
    	for _, item := range array {
    	    queue = append(queue, item)
    	}
        }
        return false
    }

