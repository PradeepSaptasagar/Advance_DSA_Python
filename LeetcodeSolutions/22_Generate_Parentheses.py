class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        def build(path, opened, closed):
            if len(path) == 2 * n:
                result.append(path)  # A complete valid sequence has been constructed.
                return
            if opened < n:
                build(path + "(", opened + 1, closed)  # Add '(' while fewer than n are used.
            if closed < opened:
                build(path + ")", opened, closed + 1)  # ')' is legal only if it closes an open '('.
        build("", 0, 0)
        return result