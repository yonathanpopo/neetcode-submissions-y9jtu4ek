class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        for s in logs:
            if s == './':
                continue
            elif s == '../':
                res = max(0, res - 1)
            else:
                res += 1
        return res