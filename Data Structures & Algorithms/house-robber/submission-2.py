class Solution:
    def rob(self, nums: List[int]) -> int:
        # H1 -> 2 | H2 -> 7 | H3 -> 9 | H4 -> 3| H5 -> 1
        money = {}
        case_1 = 0
        case_2 = 0

        lst = len(nums) % 2 == 0 

        for i in range(0, len(nums), 2):
            if lst:
                if (i + 1) > len(nums):
                    break
            case_1 += nums[i]
        
        for i in range(1, len(nums), 2):
            if not lst:
                if (i + 1) > len(nums):
                    break
            case_2 += nums[i]

        max_money = case_2 if case_2 > case_1 else case_1
        return max_money