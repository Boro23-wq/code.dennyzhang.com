# Leetcode: Additive Number     :BLOG:Medium:


---

Additive Number  

---

Similar Problems:  
-   [LintCode: K Decimal Addition](https://code.dennyzhang.com/k-decimal-addition)
-   Tag: [#manydetails](https://code.dennyzhang.com/tag/manydetails)

---

Additive number is a string whose digits can form additive sequence.  

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.  

For example:  
"112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.  

    1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

"199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.  

    1 + 99 = 100, 99 + 100 = 199

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.  

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.  

Follow up:  
How would you handle overflow for very large input integers?  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/additive-number)  

Credits To: [leetcode.com](https://leetcode.com/problems/additive-number/description/)  

Leave me comments, if you have better ways to solve.  

    // Blog link: https://code.dennyzhang.com/additive-number
    // Basic Ideas: Find all possible first two numbers.
    // The number might be overflow.
    // We may not be able to convert string to int, add them, then convert back to string.
    //
    // Complexity: Time O(n*n), Space O(n)
    import "strconv"
    
    func isAdditiveNumber2(num1 string, num2 string, num string) bool {
      if num1[0] == '0' && num1 != "0" { return false }
      if num2[0] == '0' && num2 != "0" { return false }
      num3 := addTwoStringNumber(num1, num2)
      if len(num) < len(num3) {
        return false
      } else {
        if len(num) == len(num3) {
          return num == num3
        } else {
          if num[0:len(num3)] != num3 {
            return false
          } else {
            return isAdditiveNumber2(num2, num3, num[len(num3):])
          }
        }
      }
    }
    
    func addTwoStringNumber(num1 string, num2 string) string {
      i, j, carry := len(num1)-1, len(num2)-1, 0
      res := ""
      for i>=0 && j>=0 {
        v1, _ := strconv.Atoi(string(num1[i]))
        v2, _ := strconv.Atoi(string(num2[j]))
        v := carry + v1 + v2
        if v >= 10 {
          carry = 1
          v -= 10
        } else {
          carry = 0
        }
        res = fmt.Sprintf("%d", v) + res
        i, j = i-1, j-1
      }
    
      // add the remaining string
      num := ""
      if i>=0 {
        num = num1[0:i+1]
      }
    
      if j>=0 {
        num = num2[0:j+1]
      }
    
      if num == "" {
        if carry == 1 {
          res = "1" + res
        }
      } else {
        if (carry == 0) {
          res = num + res
        } else {
          for i := len(num)-1; i>=0; i-- {
            v, _ := strconv.Atoi(string(num[i]))
            v += carry
            if v>= 10 {
              carry = 1
              v -= 10
            } else {
              carry = 0
            }
            res = fmt.Sprintf("%d", v) + res
          }
          if carry == 1 {
            res = "1" + res
          }
        }
      }
      return res
    }
    
    func isAdditiveNumber(num string) bool {
      // first number: num[0:i]
      // second number: num[i:j]
      for i := 1; i<len(num)-1; i++ {
        for j := i+1; j<len(num); j++ {
          if isAdditiveNumber2(num[0:i], num[i:j], num[j:]) {
            return true
          }
        }
      }
      return false
    }