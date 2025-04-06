import java.util.*;
import java.lang.*;

public class Solution {
    public int greatestCommonDivisor(int a, int b) {
        if (a == 0 || b == 0) {
            return a + b;
        }
        if (a == b) {
            return a;
        }
        if (a > b) {
            return greatestCommonDivisor(a % b, b);
        } else {
            return greatestCommonDivisor(a, b % a);
        }
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            int n = Integer.parseInt(args[0]);
            int o = Integer.parseInt(args[1]);
    int result = solution.greatestCommonDivisor(n, o);
    System.out.println(result);
    }
}
