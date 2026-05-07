class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1, count2 = Counter(nums1), Counter(nums2)

        res = []
        for k in count1.keys():
            if k in count2:
                res.append(k)

        return res