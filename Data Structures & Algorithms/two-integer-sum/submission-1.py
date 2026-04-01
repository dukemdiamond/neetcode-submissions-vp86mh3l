class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key: num | val: inde
        hm = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in hm:
                return [hm[difference], i]
            hm[num] = i


