# Leetcode: Minimum Index Sum of Two Lists     :BLOG:Amusing:


---

Minimum Index Sum of Two Lists  

---

Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.  

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.  

    Example 1:
    Input:
    ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    Output: ["Shogun"]
    Explanation: The only restaurant they both like is "Shogun".

    Example 2:
    Input:
    ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    ["KFC", "Shogun", "Burger King"]
    Output: ["Shogun"]

Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).  
Note:  
1.  The length of both lists will be in the range of [1, 1000].
2.  The length of strings in both lists will be in the range of [1, 30].
3.  The index is starting from 0 to the list length minus 1.
4.  No duplicates in both lists.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/minimum-index-sum-of-two-lists)  

Credits To: [leetcode.com](https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/minimum-index-sum-of-two-lists
    class Solution(object):
        def findRestaurant(self, list1, list2):
            """
            :type list1: List[str]
            :type list2: List[str]
            :rtype: List[str]
            """
            ## Idea:
            ## Complexity: Time O(n*n), Space O(1)
            sum_list = []
            item_list = []
            for i in range(0, len(list1)):
                word1 = list1[i]
                for j in range(0, len(list2)):
                    word2 = list2[j]
                    if word1 == word2:
                        sum_list.append(i+j)
                        item_list.append(word1)
                        break
    
            min_sum = sum_list[0]
            for i in range(1, len(sum_list)):
                if min_sum > sum_list[i]:
                    min_sum = sum_list[i]
            ret = []
            for i in range(0, len(sum_list)):
                if min_sum == sum_list[i]:
                    ret.append(item_list[i])
            return ret