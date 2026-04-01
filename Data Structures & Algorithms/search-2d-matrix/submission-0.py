from typing import List
'''
Leetcode: Search a 2D Matrix

You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?

'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        I'm thinking of how we can run binary search on this.
        It's a 2D Matrix, which is sorted by row.
        
        We first could check which row it would belong to by seeing whether the target is greater
        than the first idx of the row. This is because everything to the right of that idx is > than it,
        and everything below it is less.

        1. Find what row it is in
        - loop through # of rows and if < target, eliminate that row.
            - This seems naive and would run in O(n) time due to its looping
        
        We really just need to form-fit binary search into 2D array style. What does that look like?
        Run the same binary search but for each row? Since they're separated into diff lists?
        '''
        for i, row in enumerate(matrix):
            l = 0
            r = len(row) - 1
            # needs to be <= to account for when it's just 1
            while l <= r:
                m = (l+r) // 2
                if target > row[m]:
                    l = m + 1
                elif target < row[m]:
                    r = m - 1
                else:
                    # double check
                    print(f"Row: {i}, Index {m}")
                    return True

        return False
        
matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 10
s = Solution()
cond = s.searchMatrix(matrix, target)
print(cond)

# What is this time complexity?