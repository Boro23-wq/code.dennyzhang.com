# Leetcode: Sequence Reconstruction     :BLOG:Medium:


---

Sequence Reconstruction  

---

Similar Problems:  
-   [Letter Case Permutation](https://brain.dennyzhang.com/letter-case-permutation)
-   [Review: Combinations and Permutations Problems](https://brain.dennyzhang.com/review-combination), [Tag: #combination](https://brain.dennyzhang.com/tag/combination)
-   [Review: Game Problems](https://brain.dennyzhang.com/review-game), [Tag: #game](https://brain.dennyzhang.com/tag/game)

---

Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 104. Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it). Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.  

Example 1:  

    Input:
    org: [1,2,3], seqs: [[1,2],[1,3]]
    
    Output:
    false
    
    Explanation:
    [1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.

Example 2:  

    Input:
    org: [1,2,3], seqs: [[1,2]]
    
    Output:
    false
    
    Explanation:
    The reconstructed sequence can only be [1,2].

Example 3:  

    Input:
    org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]
    
    Output:
    true
    
    Explanation:
    The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].

Example 4:  

    Input:
    org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]
    
    Output:
    true

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/sequence-reconstruction)  

Credits To: [leetcode.com](https://leetcode.com/problems/sequence-reconstruction/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/sequence-reconstruction