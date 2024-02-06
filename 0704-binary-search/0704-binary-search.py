class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        mid = 0
        high = len(nums) - 1
        
        # Implement binary search.
        while (low <= high):
            mid = int((low + high) / 2)
            if nums[mid] == target:
                return mid
            elif (nums[mid] > target):
                high = mid - 1
            else:
                low = mid + 1
        
        return -1