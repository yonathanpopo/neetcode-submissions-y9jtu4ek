class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        visit = set()
        for d in path:
            visit.add((x, y))
            if d == 'N':
                y += 1
            elif d == 'S':
                y -= 1
            elif d == 'E':
                x += 1
            elif d == 'W':
                x -= 1
            if (x, y) in visit: return True
        return False