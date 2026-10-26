from collections import deque

class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        if not grid or not grid[0]:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        divisible_islands = 0
        
        for r in range(rows):
            for c in range(cols):
                # When we hit an unvisited positive cell, start BFS
                if grid[r][c] > 0:
                    island_sum = 0
                    queue = deque([(r, c)])
                    
                    # Add to sum and sink immediately to prevent duplicate enqueues
                    island_sum += grid[r][c]
                    grid[r][c] = 0 
                    
                    while queue:
                        curr_r, curr_c = queue.popleft()
                        
                        # Check top, bottom, left, right
                        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nr, nc = curr_r + dr, curr_c + dc
                            
                            # If within bounds and positive
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > 0:
                                island_sum += grid[nr][nc]
                                grid[nr][nc] = 0  # Mark visited immediately
                                queue.append((nr, nc))
                                
                    # After BFS completes, check divisibility
                    if island_sum % k == 0:
                        divisible_islands += 1
                        
        return divisible_islands

# Time Complexity=O(m*n), Space Complexity=O(m*n)

class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        if not grid or not grid[0]:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        divisible_islands = 0
        
        # Traversal helper to sum connected components
        def dfs(r, c):
            # Stop if out of bounds or if we hit water/visited cell (<= 0)
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] <= 0:
                return 0
            
            current_val = grid[r][c]
            # Mark as visited by sinking it to 0
            grid[r][c] = 0
            
            # Sum the current value with all connected positive cells
            return (current_val + 
                    dfs(r - 1, c) + 
                    dfs(r + 1, c) + 
                    dfs(r, c - 1) + 
                    dfs(r, c + 1))
                    
        # Sweep the entire grid
        for r in range(rows):
            for c in range(cols):
                # When we hit an unvisited positive cell, a new island starts
                if grid[r][c] > 0:
                    island_sum = dfs(r, c)
                    
                    # Check if the total sum of this island is divisible by k
                    if island_sum % k == 0:
                        divisible_islands += 1
                        
        return divisible_islands
        
# Time Complexity=O(m*n), Space Complexity=O(m*n)
