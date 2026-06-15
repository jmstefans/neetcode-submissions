class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search the first column for which row the target could be in
        # then binary search the row 

        l, r = 0, len(matrix) - 1
        possibleRowIndex = -1

        while l <= r and possibleRowIndex == -1:
            m = (l + r) // 2 # round to floor
            if matrix[m][0] < target:
                # could be in this row so check
                #if m + 1 < len(matrix) and target < matrix[m + 1][0]:
                if target <= matrix[m][len(matrix[0]) - 1]:
                    possibleRowIndex = m
                else:
                    l = m + 1
            elif matrix[m][0] > target:
                r = m - 1
            else:
                return True # covers the case where the target is in the first column

        # if we're here then we have a possibleRowIndex to binary search through
        l, r = 0, len(matrix[0]) - 1

        while l <= r:
            m = (l + r) // 2
            if matrix[possibleRowIndex][m] < target:
                l = m + 1
            elif matrix[possibleRowIndex][m] > target:
                r = m - 1
            else:
                return True

        return False