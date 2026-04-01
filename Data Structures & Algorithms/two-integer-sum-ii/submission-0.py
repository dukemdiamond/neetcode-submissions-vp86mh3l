class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        numbers = [1,2,3,4]
        We want the indexes, so that they add up to a number target
        So if target was 3,
        1+2 = 3

        We could use two pointer ot go from left to right, since its already sorted we can just store those in a hash map
        '''
        l = 0 
        r = len(numbers) - 1
        while l < r:
            difference = target - numbers[l]
            if numbers[r] > difference:
                r-= 1
            else:
                if numbers[r] == difference:
                    return [l + 1, r + 1]
                else:
                    l += 1
