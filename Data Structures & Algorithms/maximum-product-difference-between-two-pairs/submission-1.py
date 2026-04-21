class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()

        product1 = nums[len(nums)-1] * nums[len(nums)-2]
        product2 = nums[0] * nums[1]

        return product1 - product2