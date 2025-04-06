import java.util.*;
import java.lang.*;

public class Solution {
    public boolean correctBracketing(String brackets) {
        int depth = 0;
        for (char b : brackets.toCharArray()) {
            if (b == '<') {
                depth += 1;
            } else {
                depth -= 1;
            }
            if (depth < 0) {
                return false;
            }
        }
        return depth == 0;
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            String n = args[0];
    boolean result = solution.correctBracketing(n);
    System.out.println(result);
    }
}
