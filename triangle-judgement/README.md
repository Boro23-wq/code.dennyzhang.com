# Leetcode: Triangle Judgement     :BLOG:Basic:


---

Triangle Judgement  

---

Similar Problems:  
-   [Review: SQL Problems](https://code.dennyzhang.com/review-sql), [Tag: #sql](https://code.dennyzhang.com/tag/sql)

---

A pupil Tim gets homework to identify whether three line segments could possibly form a triangle.  
However, this assignment is very heavy because there are hundreds of records to calculate.  
Could you help Tim by writing a query to judge whether these three sides can form a triangle, assuming table triangle holds the length of the three sides x, y and z.  

    | x  | y  | z  |
    |----|----|----|
    | 13 | 15 | 30 |
    | 10 | 20 | 15 |

For the sample data above, your query should return the follow result:  

    | x  | y  | z  | triangle |
    |----|----|----|----------|
    | 13 | 15 | 30 | No       |
    | 10 | 20 | 15 | Yes      |

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/triangle-judgement)  

Credits To: [leetcode.com](https://leetcode.com/problems/triangle-judgement/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/triangle-judgement
    select x, y, z,
           case
               when x+y>z and y+z>x and x+z>y then 'Yes'
               else 'No'
           end as triangle
    from triangle
    
    ## Basic Ideas: max(x, y, z) < sum(x, y, z)/2
    # select x, y, z, if(max_value<sum_value/2, 'Yes', 'No') as triangle
    # from (
    #     select *, x+y+z as sum_value,
    #         case
    #             when x>=y and x>=z then x
    #             when y>=x and y>=z then y
    #             when z>=x and z>=y then z
    #             else x
    #         end as max_value
    #     from triangle) as t