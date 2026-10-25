class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        
        # Traversal helper function (Depth-First Search)
        def dfs(r, c):
            # Stop if out of bounds or if we hit water (1)
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 1:
                return
            
            # Mark current 0 as visited by turning it into a 1
            grid[r][c] = 1 
            
            # Traverse top, bottom, left, right
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
            
        # 1. Border Elimination
        # Sweep the outer edges. If a 0 is found, run DFS to turn the entire connected island to 1s.
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and grid[r][c] == 0:
                    dfs(r, c)
                    
        # 2. Inner Grid Sweep and Island Counting
        closed_islands = 0
        # We can skip the outer bounds now since they are processed (range starts at 1, ends at -1)
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if grid[r][c] == 0:
                    closed_islands += 1
                    # 3. Connected Marking: sink this island so it isn't counted again
                    dfs(r, c) 
                    
        return closed_islands

# Time Complexity=O(m*n)=O(N), where N=m*n
# Space Complexity=O(m*n)=O(N), where N=m*n

import collections

class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        
        # BFS helper using a double-ended queue
        def bfs(r, c):
            queue = collections.deque([(r, c)])
            grid[r][c] = 1  # Mark as visited immediately
            
            while queue:
                curr_r, curr_c = queue.popleft()
                
                # Check all 4 directions iteratively
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = curr_r + dr, curr_c + dc
                    
                    # If neighbor is within bounds and is land (0), queue it up
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                        grid[nr][nc] = 1  # Mark visited to prevent infinite loops
                        queue.append((nr, nc))
                        
        # 1. Border Elimination
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and grid[r][c] == 0:
                    bfs(r, c)
                    
        # 2. Inner Grid Sweep and Island Counting
        closed_islands = 0
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if grid[r][c] == 0:
                    closed_islands += 1
                    bfs(r, c)
                    
        return closed_islands

# Time Complexity=O(m*n)=O(N), where N=m*n
# Space Complexity=O(m*n)=O(N), where N=m*n

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
        
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            # Always attach to the smaller root to prioritize the boundary dummy node (index 0)
            if root_i < root_j:
                self.parent[root_j] = root_i
            else:
                self.parent[root_i] = root_j

class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        # dummy node at index 0 represents the boundary
        dsu = DSU(rows * cols + 1)
        
        def get_id(r, c):
            return r * cols + c + 1
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    curr_id = get_id(r, c)
                    # Union with dummy node (0) if on the boundary
                    if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                        dsu.union(0, curr_id)
                    
                    # Union with adjacent 0s (only need to check up and left to avoid redundant operations)
                    if r > 0 and grid[r-1][c] == 0:
                        dsu.union(curr_id, get_id(r-1, c))
                    if c > 0 and grid[r][c-1] == 0:
                        dsu.union(curr_id, get_id(r, c-1))
                        
        closed_islands = 0
        # Check all internal cells; count roots that are not connected to the dummy node
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if grid[r][c] == 0 and dsu.parent[get_id(r, c)] == get_id(r, c):
                    if dsu.find(get_id(r, c)) != 0:
                        closed_islands += 1
                        
        return closed_islands

# Time Complexity=O(m*n*α(m*n))=O(N), where N=m*n
# Space Complexity=O(m*n)=O(N), where N=m*n