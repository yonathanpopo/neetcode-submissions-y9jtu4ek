class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapa = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in mapa:
                return [mapa[diff], i]
            mapa[nums[i]] = i
        