class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for row in range(n):
            for column in range(n):
                matrix[row].insert(0, matrix[column].pop(-1))
        matrix.reverse()