from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for l in range(len(nums) - 2):
            if l > 0 and nums[l] == nums[l - 1]:
                continue
            
            i, r = l + 1, len(nums) - 1
            while i < r:
                s = nums[l] + nums[i] + nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    i += 1
                else:
                    res.append([nums[l], nums[i], nums[r]])
                    i += 1
                    while nums[i] == nums[i - 1] and i < r:
                        i += 1
        
        return res

# Test
solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
print(solution.threeSum([])) # []
print(solution.threeSum([0])) # []
print(solution.threeSum([0,0,0])) # [[0,0,0]]