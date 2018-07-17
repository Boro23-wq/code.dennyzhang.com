
# Leetcode: Permutation Sequence     :BLOG:Medium:

---

Permutation Sequence  

---

Similar Problems:  

-   [Next Permutation](https://code.dennyzhang.com/next-permutation)
-   [Review: Combinations and Permutations Problems](https://code.dennyzhang.com/review-combination)
-   Tag: [#combination](https://code.dennyzhang.com/tag/combination)

---

The set [1,2,3,&#x2026;,n] contains a total of n! unique permutations.  

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:  

1.  "123"
2.  "132"
3.  "213"
4.  "231"
5.  "312"
6.  "321"

Given n and k, return the kth permutation sequence.  

Note:  

-   Given n will be between 1 and 9 inclusive.
-   Given k will be between 1 and n! inclusive.

Example 1:  

    Input: n = 3, k = 3
    Output: "213"

Example 2:  

    Input: n = 4, k = 9
    Output: "2314"

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/permutation-sequence)  

Credits To: [leetcode.com](https://leetcode.com/problems/permutation-sequence/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/permutation-sequence
    // Basic Ideas:
    // For length of k, there are k! combinations
    // We can decide the digits from left to right
    // l: array of bool with n elements
    // l[i] means whether i+1 has been taken
    //
    // 1234, n=4, k=9
    // X X X X
    //       1
    //     2
    //   6
    // 24
    //  n=4, k=1
    //   1=0*6+0*2+0*1+1 1234
    //
    //  n=4, k=2
    //   2=0*6+0*2+1*1+1
    //
    //  n=4, k=5
    //   9 = 0*6+2*2+0*1+1
    //       1423
    //
    //  n=4, k=9
    //   9 = 1*6+1*2+0*1+1
    //       2314
    //
    // Complexity: Time O(n), Space O(n)
    func getPermutation(n int, k int) string {
      res := ""
      l := make([]bool, n)
      // get (n-1)!
      v := 1
      for i:= 1; i<n; i++ { v = v*i }
      k -= 1
      num := n-1
      for k!=0 {
        if v>k {
          // choose the least one
          for j:=0; j<n; j++ {
    	if l[j] == false {
    	  res = fmt.Sprintf("%s%d", res, j+1)
    	  l[j] = true
    	  break
    	}
          }
        } else {
          // k>=v: need to customize current digit
          index := int(k/v)
          for j:=0; j<n; j++ {
    	if l[j] == false {
    	  if index == 0 {
    	    res = fmt.Sprintf("%s%d", res, j+1)
    	    l[j] = true
    	    break
    	  }
    	  index -= 1
    	}
          }
          k -= v*int(k/v)
        }
        v = int(v/num)
        num--
      }
    
      // collect results
      for i:=0; i<n; i++ {
        if l[i] == false {
          res = fmt.Sprintf("%s%d", res, i+1)
        }
      }
      return res
    }

