
# Leetcode: Minimum Factorization     :BLOG:Medium:

---

Minimum Factorization  

---

Similar Problems:  

-   Tag: [#math](https://code.dennyzhang.com/tag/math)

---

Given a positive integer a, find the smallest positive integer b whose multiplication of each digit equals to a.  

If there is no answer or the answer is not fit in 32-bit signed integer, then return 0.  
Example 1  

    Input:
    
    48 
    Output:
    68

Example 2  

    Input:
    
    15
    Output:
    35

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/minimum-factorization)  

Credits To: [leetcode.com](https://leetcode.com/problems/minimum-factorization/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/minimum-factorization
    // Basic Ideas:
    //
    // 48 -> [2, 2, 2, 2, 2, 3]
    // 15 -> [3, 5]
    //
    // If n has dividends bigger than 9, it won't work
    //
    // Now we get all dividends as l[int]. 
    // How we can construct the minimum number?
    // - smallest digits count
    // - smallest digit values
    //
    // Complexity:
    func smallestFactorization(a int) int {
        if a<=1 { return a }
        m := map[int]int{}
        for _, v:=range[]int{2, 3, 5, 7} {
    	for a%v == 0 {
    	    a = int(a/v)
    	    m[v] += 1
    	}
        }
        if a !=1 { return 0 }
    
        // 2 2 2 -> 8
        if m[2] >= 3 { m[8], m[2] =int(m[2]/3), m[2]%3 }
        // 3 3 -> 9
        if m[3] >=2 { m[9],m[3] = int(m[3]/2), m[3]%2 }
        // 2 3 -> 6
        if m[2]>=1 && m[3]==1 { m[6], m[2], m[3] = 1, m[2]-1, 0 }
        // 2 2 -> 4
        if m[2]==2 { m[2], m[4] = 0, 1 }
        // get the result
        res := 0
        for i:=2; i<10; i++ {
    	for m[i] != 0 {
    	    res = res*10+i
    	    if res > 2147483647 { return 0 }
    	    m[i]--
    	}
        }
        return res
    }

