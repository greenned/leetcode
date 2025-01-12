class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        new_matrix = []
        for m in matrix:
            new_matrix.extend(m)

        if target in new_matrix:
            return True
        return False
        