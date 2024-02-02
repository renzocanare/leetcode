# nums - INT_ARRAY
# target - INT

# # Brute force (Time: O(n^2)):
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(0, len(nums) - 1):
#             for j in range(1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

# Hash Table (Time: O(n)):
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nMap = {}  # Hash Table
        n = len(nums)

        for i in range(n):
            # Get complement to check if it exists in Hash Table.
            complement = target - nums[i]

            # If complement in Hash Table, return the pair.
            if complement in nMap:
                return [nMap[complement], i]

            # If not, store it in Hash Table.    
            nMap[nums[i]] = i
        
        return [] # No solution found.
