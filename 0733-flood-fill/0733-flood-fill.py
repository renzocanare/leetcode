class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        srcColor = image[sr][sc]
        seen = set()
        
        def fillCell(row, col):
            currColor = image[row][col]
            if currColor != srcColor or (row, col) in seen:
                # If curr cell has a different color than original or has been seen before, return.
                return
            else:
                # If not, then it must be the correct next cell.
                # Update the color of this cell to the new color.
                image[row][col] = color
                seen.add((row, col))
                
                # Recursive DFS to fill all 4-directionally adjacent cells that are of the same starting color.
                for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # Up, down, left, right.
                    nextRow = row + dir[0]
                    nextCol = col + dir[1]
                    if (0 <= nextRow < len(image)) and (0 <= nextCol < len(image[0])):
                        fillCell(nextRow, nextCol)
                    else:
                        continue
        
        fillCell(sr, sc)
        return image
            