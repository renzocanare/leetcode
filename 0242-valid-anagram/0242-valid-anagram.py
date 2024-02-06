class Solution:
    def isAnagram(self, s: str, t: str) -> bool: 
        if len(s) != len(t):
            # If the lengths of the text are not equal, it cannot be an anagram.
            return False
        
        if ''.join(sorted(s)) == ''.join(sorted(t)):
            # If the alphabetically sorted strings are equal, it means they can be an anagram of each other.
            return True
        else:
            return False