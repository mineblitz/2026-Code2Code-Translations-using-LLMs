import java.util.*;
import java.lang.*;

public class Solution {
    public boolean isHappy(String s) {
        if (s.length() < 3) {
            return false;
        }

        for (int i = 0; i < s.length() - 2; i++) {
            if (s.charAt(i) == s.charAt(i + 1) || s.charAt(i + 1) == s.charAt(i + 2) || s.charAt(i) == s.charAt(i + 2)) {
                return false;
            }
        }
        return true;
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            String n = args[0];
    boolean result = solution.isHappy(n);
    System.out.println(result);
    }
}
