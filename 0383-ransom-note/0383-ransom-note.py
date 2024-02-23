class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letterMap = {}  # Map to store letter counts.
        
        # Store character counts into letterMap.
        for char in magazine:
            if char in letterMap:
                letterMap[char] += 1
            else:
                letterMap[char] = 1
        
        # Check if can rebuild ransomNote using letterMap.
        for char in ransomNote:
            if char not in letterMap or letterMap[char] <= 0:
                # If there are missing characters or that particular character has no more usable counts,
                # return False.
                return False
            else:
                letterMap[char] -= 1
        
        # If can successfully rebuild string, return True.
        return True
        