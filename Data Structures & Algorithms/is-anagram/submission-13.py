class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return False if Counter(s) != Counter(t) else True