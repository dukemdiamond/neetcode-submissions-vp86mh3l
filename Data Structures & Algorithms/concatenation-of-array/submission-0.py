class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # We're given 
        # n = (len(nums))
        # ans = [0] * (2*n)

        # for i in range(len(ans)):
        #     ans[i] = nums[(i % n)]
        # return ans
        
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans