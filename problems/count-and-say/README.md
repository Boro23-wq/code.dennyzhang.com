
# Leetcode: Count and Say     :BLOG:Medium:

---

Count and Say  

---

Similar Problems:  

-   Tag: [#padplaceholder](https://code.dennyzhang.com/tag/padplaceholder), [#string](https://code.dennyzhang.com/tag/string)

---

The count-and-say sequence is the sequence of integers with the first five terms as following:  

    1.     1
    2.     11
    3.     21
    4.     1211
    5.     111221

    1 is read off as "one 1" or 11.
    11 is read off as "two 1s" or 21.
    21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth term of the count-and-say sequence.  

Note: Each term of the sequence of integers will be represented as a string.  

    Example 1:
    
    Input: 1
    Output: "1"

    Example 2:
    
    Input: 4
    Output: "1211"

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/count-and-say)  

Credits To: [leetcode.com](https://leetcode.com/problems/count-and-say/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/count-and-say
    // Basic Ideas:
    //   From n-1 to n
    //       1.     1
    //       2.     11
    //       3.     21
    //       4.     1211
    //       5.     111221 
    //       6.     312211
    //       7.     13112221
    //       8.     1113213211
    //       9.     31131211131221
    //      10.     13211311123113112211
    // Complexity: Time O(n), Space O(m)
    //    m = length of target string
    func countAndSay(n int) string {
        if n == 1 { return "1" }
        l := []string{"1"}
        for i:=1; i<n; i++ {
    	l2 := []string{}
    	count := 1
    	l = append(l, " ")
    	for i, ch := range l {
    	    if i == 0 { continue }
    	    if ch != l[i-1] {
    		l2 = append(l2, strconv.Itoa(count))
    		l2 = append(l2, l[i-1])
    		count = 1
    	    } else {
    		count++
    	    }
    	}
    	l = l2
        }
        return strings.Join(l, "")
    }

