class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().strip()
        
        # Remove non-alphanumeric characters and spaces.
        cleanedText = [char for char in s if char.isalnum()]
        cleanedText = "".join(cleanedText)

        # If empty string, return True.
        if not cleanedText:
            return True
        
        # Using two pointers, check left and right until they meet in the middle.
        lPtr = 0
        for rPtr in range(len(cleanedText) - 1, -1, -1):
            if lPtr >= rPtr:
                return True
            
            if cleanedText[lPtr] == cleanedText[rPtr]:
                lPtr += 1
            else:
                return False
                