class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # we use bucket sort
        # The count for how many of each number
        counts = [0] * len(nums)


        # Let's initialize how many times each number shows up
        if len(nums) <= 1:
            return nums
        for n in nums:
            counts[n] += 1

        i = 0
        # Go through each number 
        for n in range(len(nums)):
            # Go through how many times it appears
            for j in range(counts[n]):
                nums[i] = n
                i+=1
            
        