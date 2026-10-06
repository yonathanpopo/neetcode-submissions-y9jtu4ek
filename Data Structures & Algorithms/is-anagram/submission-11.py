class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for c in s:
            if c not in count:
                count[c] = 0
            count[c] += 1

        for i in range(len(t)):
            c = t[i]
            if c not in count:
                return False
            if count[c] == 0:
                return False
            count[c] -= 1

        return True