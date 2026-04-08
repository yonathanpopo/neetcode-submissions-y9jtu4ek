class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = []
        l, r = 0, k-1
        minDiff = float('inf')
        while r < len(nums):
            diff = nums[r] - nums[l]
            if diff < minDiff:
                res = nums[l:r+1]
                minDiff = diff
            l += 1
            r = l+k-1

        return minDiff