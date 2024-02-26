class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        # Build hash table.
        charMap = {}
        for char in s:
            if char not in charMap:
                charMap[char] = 1
            else:
                charMap[char] += 1
        
        # Get max length of palindrome.
        maxLength = 0
        singleChar = False
        resMap = charMap.copy()
        
        for char in charMap:
            if len(charMap) == 1:
                return charMap[char]
            
            if (charMap[char] % 2 == 0):
                maxLength += charMap[char]
                del resMap[char]
            else:
                if (charMap[char] != 1):
                    toAdd = resMap[char] - 1
                    maxLength += toAdd
                    resMap[char] -= toAdd
        
        if resMap:
            maxLength += 1
            
        return maxLength