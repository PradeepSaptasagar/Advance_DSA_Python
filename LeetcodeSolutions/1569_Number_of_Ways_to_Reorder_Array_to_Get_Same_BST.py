import math

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7

        def ways(arr: list[int]) -> int:
            # Base condition: lists with <= 2 elements have only 1 way to form the BST
            if len(arr) <= 2:
                return 1

            # Isolate root and partition into subtrees
            n = len(arr)
            root_node = arr[0]
            left_list = []
            right_list = []

            for i in range(1, n):
                if arr[i] < root_node:
                    left_list.append(arr[i])
                elif arr[i] > root_node:
                    right_list.append(arr[i])

            # Interleaving combinations: choose len(left_list) slots out of (L + R) total slots
            total_slots = len(left_list) + len(right_list)
            interleave = math.comb(total_slots, len(left_list))

            # Recursive step: multiply choices across subproblems
            return (interleave * ways(left_list) * ways(right_list)) % MOD

        # Subtract 1 to exclude the original array ordering
        return (ways(nums) - 1) % MOD

# Time Complexity=O(N^2), Space Complexity=O(N^2)

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # 1. Build the BST
        root = TreeNode(nums[0])
        for val in nums[1:]:
            curr = root
            while True:
                if val < curr.val:
                    if curr.left is None:
                        curr.left = TreeNode(val)
                        break
                    curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = TreeNode(val)
                        break
                    curr = curr.right

        # 2. Collect subtree sizes via Post-Order Traversal
        subtree_sizes = []

        def get_sizes(node: TreeNode) -> int:
            if not node:
                return 0
            left_size = get_sizes(node.left)
            right_size = get_sizes(node.right)
            total_size = 1 + left_size + right_size
            subtree_sizes.append(total_size)
            return total_size

        get_sizes(root)

        # 3. Compute (N! / product(subtree_sizes)) % MOD using modular inverse
        numerator = 1
        for i in range(1, n + 1):
            numerator = (numerator * i) % MOD

        denominator = 1
        for size in subtree_sizes:
            denominator = (denominator * size) % MOD

        # Fermat's Little Theorem for modular division: a / b = a * pow(b, MOD - 2, MOD)
        total_ways = (numerator * pow(denominator, MOD - 2, MOD)) % MOD

        return (total_ways - 1) % MOD

# Time Complexity=O(N^2), Space Complexity=O(N^2)