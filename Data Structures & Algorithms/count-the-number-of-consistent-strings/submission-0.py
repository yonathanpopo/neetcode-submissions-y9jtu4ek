class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        real = set(c for c in allowed)

        res = len(words)
        for w in words:
            for c in w:
                if c not in real:
                    res -= 1
                    break
        return res