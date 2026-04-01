class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n^2): We can use a nested for loop to check all indices of the nums list
    
        prevMap = {} # (key) val : (val) index 

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i] # diff first cause it must be a smaller index
            prevMap[n] = i
        



            


        