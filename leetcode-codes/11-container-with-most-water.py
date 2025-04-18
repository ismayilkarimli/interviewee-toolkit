from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0

        while l < r:
            area = (r - l) * min(height[l], height[r])
            max_area = max(area, max_area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return max_area

solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7])) # 49
print(solution.maxArea([1,1])) # 1
