import java.util.*;
import java.lang.*;

public class Solution {
    public int fizzBuzz(int n) {
        int result = 0;
        for (int i = 1; i < n; i++) {
            if (i % 11 == 0 || i % 13 == 0) {
                char[] digits = String.valueOf(i).toCharArray();
                for (char c : digits) {
                    if (c == '7') {
                        result += 1;
                    }
                }
            }
        }
        return result;
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            int n = Integer.parseInt(args[0]);
    int result = solution.fizzBuzz(n);
    System.out.println(result);
    }
}
