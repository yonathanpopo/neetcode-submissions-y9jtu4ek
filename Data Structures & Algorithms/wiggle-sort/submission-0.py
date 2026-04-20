class Solution:
    def wiggleSort(self, nums: List[int]) -> None:

        for i in range(1, len(nums)):
            if ((i % 2 and nums[i] < nums[i-1]) or
                (not (i % 2) and nums[i] > nums[i-1])):
                tmp = nums[i]   
                nums[i] = nums[i-1]
                nums[i-1] = tmp

                