class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1

        res = 0
        while r > 0 and people[r] == limit:
            res += 1
            r -= 1
            
        while l <= r:
            diff = limit - people[r]
            res += 1
            r -= 1
            if l <= r and diff >= people[l]:
                l += 1
        return res
