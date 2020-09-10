'''Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:
Input: 
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Output: 4'''

class Solution:
    def maximalSquare(self, M: List[List[str]]) -> int:
        if not M:
            return 0
        R = len(M) 
        C = len(M[0]) 
        ans = 0
        S = [[0 for k in range(C+1)] for l in range(R+1)] 
        for i in range(1, R+1): 
            for j in range(1, C+1): 
                if (M[i-1][j-1] == "1" ): 
                    S[i][j] = min(S[i][j-1], S[i-1][j], S[i-1][j-1]) + 1
                    ans = max(ans, S[i][j])
        return ans*ans
