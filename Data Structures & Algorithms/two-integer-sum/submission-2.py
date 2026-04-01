class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [3,4,5,6]
        # target = 7
        # 3 + 4 = 7
        # check 3. If diff in list, 
        num_map = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in num_map:
                return [num_map[diff], i]
            num_map[num] = i


            
