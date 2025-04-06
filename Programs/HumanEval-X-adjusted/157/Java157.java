import java.util.*;
import java.lang.*;

public class Solution {
    public boolean rightAngleTriangle(int a, int b, int c) {
        return a * a == b * b + c * c || b * b == a * a + c * c || c * c == a * a + b * b;
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            int n = Integer.parseInt(args[0]);
            int o = Integer.parseInt(args[1]);
            int p = Integer.parseInt(args[2]);
    boolean result = solution.rightAngleTriangle(n, o, p);
    System.out.println(result);
    }
}
