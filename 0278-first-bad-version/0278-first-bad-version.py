# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        
        if n == 1 or isBadVersion(1):
            # If there is only one version or the first version is bad, return the first version.
            return 1
            
        while (low <= high):
            mid = int((low + high) / 2)
            
            if isBadVersion(mid) and not isBadVersion(mid - 1):
                # If mid is bad and the version before it is not, that is the start
                # of the bad versions. Return mid.
                return mid
            elif isBadVersion(mid):
                # If mid is a bad, then it must be on the left. 
                high = mid - 1
            else:
                # If not, then the it must be on the right.
                low = mid + 1
            
        return mid
    
