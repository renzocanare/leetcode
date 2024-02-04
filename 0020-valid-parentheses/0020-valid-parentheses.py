# s - STRING

class Solution:
    def isValid(self, s: str) -> bool:
        # Use a stack to LIFO to ensure the opening is properly closed.
        stack = []
        
        openBracket = '([{'
        closeBracket = ')]}'
        
        for char in s:
            if char in closeBracket:
                # If closing character, pop stack and check if its the correspoding opening pair.
                
                if not stack:
                    # Return False if stack is empty while iterating.
                    return False

                # Peek into stack.
                top = stack[-1]

                # If the top of the stack is the corresponding opening pair, its correct so pop and continue.
                if top == openBracket[closeBracket.find(char)]:
                    stack.pop()
                else:
                    # If not, return False.
                    return False
            else:
                # If opening character, push to stack.
                stack.append(char)   

        # If stack empty after all iterations, means correct so return True.
        if not stack:
            return True
