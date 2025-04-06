import java.util.*;
import java.lang.*;

public class Solution {
    public boolean primeLength(String string) {
        int l = string.length();
        if (l == 0 || l == 1) {
            return false;
        }
        for (int i = 2; i < l; i++) {
            if (l % i == 0) {
                return false;
            }
        }
        return true;
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            String n = args[0];
    boolean result = solution.primeLength(n);
    System.out.println(result);
    }
}
