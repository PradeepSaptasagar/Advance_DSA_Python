import sys
from typing import List

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        sys.setrecursionlimit(2 * 10**5)
        n = len(parent)
        new_parent = parent.copy()

        # Step 1: Build adjacency list for the original tree
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)

        # Step 2: Top-down DFS to find the closest matching ancestor
        last_seen = {}

        def find_ancestor(u: int) -> None:
            c = s[u]
            prev = last_seen.get(c, -1)

            if prev != -1:
                new_parent[u] = prev

            last_seen[c] = u
            for v in adj[u]:
                find_ancestor(v)
            last_seen[c] = prev  # Backtrack

        find_ancestor(0)

        # Step 3: Build adjacency list for the updated tree
        new_adj = [[] for _ in range(n)]
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)

        # Step 4: Bottom-up DFS to compute subtree sizes
        answer = [0] * n

        def calc_size(u: int) -> int:
            size = 1
            for v in new_adj[u]:
                size += calc_size(v)
            answer[u] = size
            return size

        calc_size(0)
        return answer
        