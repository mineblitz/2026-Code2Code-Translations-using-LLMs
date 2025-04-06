import java.util.*;
import java.lang.*;

public class Solution {
    public int xOrY(int n, int x, int y) {
        if (n == 1) {
            return y;
        }
        for (int i = 2; i < n; i++) {
            if (n % i == 0) {
                return y;
            }
        }
        return x;
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            int n = Integer.parseInt(args[0]);
            int o = Integer.parseInt(args[1]);
            int p = Integer.parseInt(args[2]);
    int result = solution.xOrY(n, o, p);
    System.out.println(result);
    }
}
