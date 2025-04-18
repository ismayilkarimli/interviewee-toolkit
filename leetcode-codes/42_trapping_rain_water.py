from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        total_water = 0
        left_max, right_max = height[l], height[r]

        while l < r:
            if height[l] < height[r]:
                left_max = max(left_max, height[l])
                total_water += left_max - height[l]
                l += 1
            else:
                right_max = max(right_max, height[r])
                total_water += right_max - height[r]
                r -= 1
        
        return total_water


solution = Solution()
print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
print(solution.trap([4,2,0,3,2,5])) # 9