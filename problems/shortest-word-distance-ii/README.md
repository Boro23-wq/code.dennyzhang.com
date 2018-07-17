
# Leetcode: Shortest Word Distance II     :BLOG:Medium:

---

Shortest Word Distance II  

---

Similar Problems:  

-   [Shortest Word Distance](https://code.dennyzhang.com/shortest-word-distance)
-   [Shortest Word Distance III](https://code.dennyzhang.com/shortest-word-distance-iii)
-   Tag: [#oodesign](https://code.dennyzhang.com/tag/oodesign), [#hashmap](https://code.dennyzhang.com/tag/hashmap), [#classic](https://code.dennyzhang.com/tag/classic)

---

This is a follow up of [Shortest Word Distance](https://code.dennyzhang.com/shortest-word-distance). The only difference is now you are given the list of words and your method will be called repeatedly many times with different parameters. How would you optimize it?  

Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list.  

For example,  

    Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
    
    Given word1 = "coding", word2 = "practice", return 3.
    Given word1 = "makes", word2 = "coding", return 1.

Note:  
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/shortest-word-distance-ii)  

Credits To: [leetcode.com](https://leetcode.com/problems/shortest-word-distance-ii/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution: hashmap

    // Blog link: https://code.dennyzhang.com/shortest-word-distance-ii
    // Basic Ideas: hashmap
    //   The problem is literally about: Find the mininum difference of two lists
    //
    // Complexity: Time O(n), Space O(n)
    type WordDistance struct {
        index_map map[string][]int
    }
    
    func Constructor(words []string) WordDistance {
        m := map[string][]int{}
        for i, word := range words {
    	m[word] = append(m[word], i)
        }
        return WordDistance{m}
    }
    
    func (this *WordDistance) Shortest(word1 string, word2 string) int {
        list1, list2 := this.index_map[word1], this.index_map[word2]
        res := 1<<31 - 1
        i, j := 0, 0
        for i<len(list1) && j<len(list2) {
    	diff := list1[i]-list2[j]
    	if diff<0 { diff = -diff }
    	if diff<res { res = diff }
    	if list1[i]>list2[j] { 
    	    j++
    	} else { 
    	    i++
    	}
        }
        return res
    }
    
    /**
     * Your WordDistance object will be instantiated and called as such:
     * obj := Constructor(words);
     * param_1 := obj.Shortest(word1,word2);
     */

