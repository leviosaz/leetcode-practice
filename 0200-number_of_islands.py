# Problem: Find the number of islands in an grid.

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        counter = 0
        
        def getIsland(r, c):
            stack = [[r, c]]
            
            while stack:
                item = stack.pop()
                x = item[0]
                y = item[1]
                
                if grid[x][y] == "0":
                    continue
                else:
                    grid[x][y] = "0"
                
                if x > 0:
                    stack.append([x-1, y])
                if x < len(grid)-1:
                    stack.append([x+1, y])
                if y > 0:
                    stack.append([x, y-1])
                if y < len(grid[0])-1:
                    stack.append([x, y+1])
                
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    counter += 1
                    getIsland(row, col)
        
        return counter

# Time Complexity: O(n^2)
# Space Complexity: O(1)
