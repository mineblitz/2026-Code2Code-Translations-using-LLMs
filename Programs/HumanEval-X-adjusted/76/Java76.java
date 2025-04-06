import java.util.*;
import java.lang.*;

public class Solution {
    public boolean isSimplePower(int x, int n) {
        if (n == 1) {
            return x == 1;
        }
        int power = 1;
        while (power < x) {
            power = power * n;
        }
        return power == x;
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            int n = Integer.parseInt(args[0]);
            int o = Integer.parseInt(args[1]);
    boolean result = solution.isSimplePower(n, o);
    System.out.println(result);
    }
}
