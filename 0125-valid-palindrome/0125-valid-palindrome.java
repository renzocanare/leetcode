class Solution {
    public boolean isPalindrome(String s) {
        String lowerString = s.toLowerCase();
        String finalString = "";
        
        // Get only alphanumeric characters.
        for (int i = 0; i < lowerString.length(); i++) {
            char currChar = lowerString.charAt(i);
            if (Character.isAlphabetic(currChar) || Character.isDigit(currChar)) {
                finalString += currChar;
            }
        }
        
        if (finalString.isEmpty()) {
            return true;
        }
        
        // Use two pointers and see if they meet.
        int rPtr = finalString.length() - 1;
        for (int lPtr = 0; lPtr < finalString.length(); lPtr++) {
            if (lPtr >= rPtr) {
                return true;
            }
            
            if (finalString.charAt(lPtr) != finalString.charAt(rPtr)) {
                return false;
            } else {
                rPtr -= 1;
            }
        }
        return true;
    }
}