class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letterMap = {}
        for char in magazine:
            if char in letterMap:
                letterMap[char] += 1
            else:
                letterMap[char] = 1
        
        for char in ransomNote:
            if char not in letterMap or letterMap[char] <= 0:
                return False
            else:
                letterMap[char] -= 1
        
        return True
        