class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]  # Start with the entire first string as the candidate.
        for word in strs[1:]:
            while not word.startswith(prefix):  # Shrink until this word shares the prefix.
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix