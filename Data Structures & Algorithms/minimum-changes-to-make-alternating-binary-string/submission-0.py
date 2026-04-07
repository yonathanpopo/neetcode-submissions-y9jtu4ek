class Solution:
    def minOperations(self, s: str) -> int:
        s1, s2 = "", ""
        dif1, dif2 = 0, 0 
        for i in range(len(s)):
            if i % 2:
                s1 += '0'
                s2 += '1'
            else:
                s1 += '1'
                s2 += '0'
            
            if s[i] != s1[i]:
                dif1 += 1
            if s[i] != s2[i]:
                dif2 += 1
        return min(dif1, dif2)

            