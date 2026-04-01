class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        '''
        1, 2, 4, 6
        output[0] = 48
        output[1] = 24
        output[2] = 12
        output[3] = 8

        1 2 4 6
        i == 0

        0: 2 * 4 * 6 = 48 
        1: 
        '''
        pre = []
        post = []
        
        for i in range(len(nums)):
            prod = 1
            # pre
            if i != 0:
                for j in range(0, i):
                    prod *= nums[j]
            
            # post
            if i != len(nums) - 1:
                for p in range (i + 1, len(nums)):
                    prod *= nums[p]
        
            output.append(prod)

        return output





            # post
