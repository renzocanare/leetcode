import java.util.ArrayDeque;
import java.util.Deque;


class Solution {
    
    // Helper function to check for matching pairs.
    private boolean isMatching(char open, char close) {
        return (open == '(' && close == ')') ||
            (open == '{' && close == '}') ||
            (open == '[' && close == ']');
    }
    
    public boolean isValid(String s) {
        // Initialize a stack.
        Deque<Character> stack = new ArrayDeque<>();
        
        // Return false for uneven length strings.
        if ((s.length() % 2 != 0)) {
            return false;
        } 
            
        for (int i = 0; i < s.length(); i++) {
            // Get first character.
            char currChar = s.charAt(i);
            System.out.println(currChar);
            if ( currChar == ')' || currChar == '}' || currChar == ']') {
                if (stack.isEmpty() || !isMatching(stack.peekLast(), currChar)){
                    // If stack is empty or is not a matching pair, return false.
                    return false;
                } else {
                    // Pop it and continue.
                    stack.removeLast();
                }
            } else {
                // Push to stack if opening bracket.
                stack.add(currChar);
            }
        }
        // Return if stack is empty or not; all matched should be empty, otherwise it will not.
        return stack.isEmpty();
    }
}