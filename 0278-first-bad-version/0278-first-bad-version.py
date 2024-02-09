# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        mid = 0
        
        if n == 1:
            # If there is only one version, return that version.
            return 1
            
        while (low <= high):
            mid = int((low + high) / 2)
            
            if isBadVersion(mid) and not isBadVersion(mid - 1):
                return mid
            elif isBadVersion(mid):
                # If mid is a bad, then it must be on the left. 
                high = mid - 1
            else:
                # If not, then the it must be on the right.
                low = mid + 1
            
            if isBadVersion(mid) and mid == 1:
                return 1

            print(f'----------------')            
            print(f'low: {low}')
            print(f'mid: {mid}')
            print(f'high: {high}')
            print(f'----------------')
            
        return mid
    
