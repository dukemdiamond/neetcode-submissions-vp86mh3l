class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area-- height * width (i) 
        # store max area when 

        # brute force: pointer at 1, check all aras infront, store a max, then return maximum
        # two pt approach
        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            width = r - l 
            h = min(heights[l], heights[r])
            curr_area = h * width

            max_area = max(max_area, curr_area)

            # Say we have a bar 3 2 1 4
                # We are restricted to the smaller of the two bars 
                # In first case: 3 & 4. 
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1 

        return max_area