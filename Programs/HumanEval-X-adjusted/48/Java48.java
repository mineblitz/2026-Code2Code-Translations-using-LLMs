import java.util.*;
import java.lang.*;

public class Solution {
    public boolean isPalindrome(String text) {
        for (int i = 0; i < text.length(); i++) {
            if (text.charAt(i) != text.charAt(text.length() - 1 - i)) {
                return false;
            }
        }
        return true;
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            String n = args[0];
    boolean result = solution.isPalindrome(n);
    System.out.println(result);
    }
}
