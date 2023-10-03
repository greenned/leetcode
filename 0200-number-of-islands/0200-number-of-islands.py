class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        def dfs(row, col):
            if (
                row < 0
                or row >= num_rows
                or col < 0
                or col >= num_cols
                or grid[row][col] != "1"
            ):
                return

            # WHAT TO DO: After discovering, replace it
            grid[row][col] = 0

            # Search
            dfs(row + 1, col)  # southern
            dfs(row - 1, col)  # northern
            dfs(row, col + 1)  # eastern
            dfs(row, col - 1)  # western

        num_islands = 0
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == "1":
                    dfs(row, col)
                    num_islands += 1

        return num_islands