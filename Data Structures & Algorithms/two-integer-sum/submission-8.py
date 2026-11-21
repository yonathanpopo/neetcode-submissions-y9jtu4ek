class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapa = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff not in mapa:
                mapa[n] = i
            else:
                return [mapa[diff], i]
            