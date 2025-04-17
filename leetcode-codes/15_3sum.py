from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for x in range(len(nums) - 2):
            if x > 0 and nums[x] == nums[x - 1]:
                continue
            
            l, r = x + 1, len(nums) - 1

            while l < r:
                sum = nums[x] + nums[l] + nums[r]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    res.append([nums[x], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
            
        return res
# Test
solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
print(solution.threeSum([])) # []
print(solution.threeSum([0])) # []
print(solution.threeSum([0,0,0])) # [[0,0,0]]