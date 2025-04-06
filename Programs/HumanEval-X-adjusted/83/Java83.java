import java.util.*;
import java.lang.*;

public class Solution {
    public int startsOneEnds(int n) {
        if (n == 1) {
            return 1;
        }
        return 18 * (int) Math.pow(10, n - 2);
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            int n = Integer.parseInt(args[0]);
    int result = solution.startsOneEnds(n);
    System.out.println(result);
    }
}
