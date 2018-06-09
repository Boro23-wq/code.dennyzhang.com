# Leetcode: Trapping Rain Water II     :BLOG:Hard:


---

Trapping Rain Water II  

---

Similar Problems:  
-   [Trapping Rain Water](https://code.dennyzhang.com/container-water)
-   Tag: [#trappingrain](https://code.dennyzhang.com/tag/trappingrain)

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

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/trapping-rain-water-ii)  

Credits To: [leetcode.com](https://leetcode.com/problems/trapping-rain-water-ii/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution: XXX

**General Thinkings:**  


**Key Observations:**  


**Walk Through Testdata**  


    // Blog link: https://code.dennyzhang.com/trapping-rain-water-ii
    // Basic Ideas: twopass
    // Similar idea like: https://code.dennyzhang.com/trapping-rain-water
    //
    // Sample Data:
    //     [[12,13,1,12]
    //      [13,4,13,12]
    //      [13,8,10,12]
    //      [12,13,12,12]
    //      [13,13,13,13]]
    //
    // Complexity: Time O(n*m), Space O(n*m)
    func trapRainWater(heightMap [][]int) int {
        if len(heightMap) == 0 { return 0 }
    
        max_lst := make([][]int, len(heightMap))
        for i, row := range heightMap {
            max_lst[i] = make([]int, len(row))
            for j, _ := range row {
                max_lst[i][j] = 1<<31 - 1
            }
        }
    
        // get the maximum
        max := 0
        for i:= 0; i< len(heightMap); i++ {
            max = 0
            for j:= 0; j<len(heightMap[i]); j++ {
                if heightMap[i][j] > max { max = heightMap[i][j] }
                if max < max_lst[i][j] { max_lst[i][j] = max }
            }
        }
    
        for i:= 0; i< len(heightMap); i++ {
            max = 0
            for j:=len(heightMap[i])-1; j>=0; j-- {
                if heightMap[i][j] > max { max = heightMap[i][j] }
                if max < max_lst[i][j] { max_lst[i][j] = max }
            }
        }
    
        for j:= 0; j< len(heightMap[0]); j++ {
            max = 0
            for i:=0; i<len(heightMap); i++ {
                if heightMap[i][j] > max { max = heightMap[i][j] }
                if max < max_lst[i][j] { max_lst[i][j] = max }
            }
        }
    
        for j:= 0; j< len(heightMap[0]); j++ {
            max = 0
            for i:=len(heightMap)-1; i>=0; i-- {
                if heightMap[i][j] > max { max = heightMap[i][j] }
                if max < max_lst[i][j] { max_lst[i][j] = max }
            }
        }
    
        res, border := 0, 0
        // collect result
        for i:= 0; i< len(heightMap); i++ {
            for j:= 0; j<len(heightMap[i]); j++ {
                border = max_lst[i][j]
                res += border - heightMap[i][j]
            }
        }
        return res
    }