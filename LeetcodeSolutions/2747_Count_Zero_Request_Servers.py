class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        # Pair each query time with its original index, then sort by time
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])
        
        # Sort logs chronologically by time
        logs.sort(key=lambda log: log[1])
        
        ans = [0] * len(queries)
        active_servers = {}
        
        left = 0
        right = 0
        num_logs = len(logs)
        
        # Slide the window for each query
        for q_time, original_idx in sorted_queries:
            t1 = q_time - x  # Start of your interval bound
            t2 = q_time      # End of your interval bound
            
            # 1. Expand the window forward to include new logs (t <= t2)
            while right < num_logs and logs[right][1] <= t2:
                server_id = logs[right][0]
                active_servers[server_id] = active_servers.get(server_id, 0) + 1
                right += 1
                
            # 2. Shrink the window from the back to drop old logs (t < t1)
            while left < num_logs and logs[left][1] < t1:
                server_id = logs[left][0]
                active_servers[server_id] -= 1
                if active_servers[server_id] == 0:
                    del active_servers[server_id]
                left += 1
                
            # 3. Calculate inactive servers and place in the original query order
            ans[original_idx] = n - len(active_servers)
            
        return ans
    