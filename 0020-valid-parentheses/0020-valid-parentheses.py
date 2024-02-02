# s - STRING

class Solution:
    def isValid(self, s: str) -> bool:
        # Use a stack to LIFO to ensure the opening is properly closed.
        stack = []
        
        bracketMap = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        openBracket = ['(', '[', '{']
        closeBracket = [')', ']', '}']
        
        for char in s:
            if char in openBracket:
                stack.append(char)
            
            if char in closeBracket:
                if not stack:
                    return False
                
                top = stack[-1] # Peek into stack.
                
                if top == bracketMap[char]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True