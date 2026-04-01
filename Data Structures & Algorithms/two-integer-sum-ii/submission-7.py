class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        input: numbers (int array)
        return: INDICES 1 indexed [in1, in2], so they add up to target
            Cond: ind1 < ind2. ind1 != ind2. ind1 !== ind2
        
        [1,2,3,4] target = 3
        '''
        # if index 1 < index 2 

        i = 0
        j = len(numbers) - 1
        count = 0

        while i < j:
            curr_sum = numbers[i] + numbers[j]
            if curr_sum == target:
                return [i + 1, j + 1]
            if curr_sum > target:
                j-=1
            if curr_sum < target:
                i += 1
        return [0,0]



