class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for s in logs:
            if s == '../' and stack:
                stack.pop()
            elif s == './' or s == '../':
                continue
            else:
                stack.append(s)
        return len(stack)