class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res1, res2 = [], []
        
        for i in range(len(nums)):
            if nums[i] % 2:
                res2.append(nums[i])
            else:
                res1.append(nums[i])

        return res1 + res2