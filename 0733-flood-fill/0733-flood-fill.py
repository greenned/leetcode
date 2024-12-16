class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        origin_color = image[sr][sc]
        rows, cols = len(image), len(image[0])

        if origin_color == color:
            return image

        def dfs(r:int, c:int):

            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != origin_color:
                return 
            
            image[r][c] = color

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        dfs(sr, sc)
        return image

        




