import java.util.*;
import java.lang.*;

public class Solution {
    public int largestDivisor(int n) {
        for (int i = n - 1; i > 0; i--) {
            if (n % i == 0) {
                return i;
            }
        }
        return 1;
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            int n = Integer.parseInt(args[0]);
    int result = solution.largestDivisor(n);
    System.out.println(result);
    }
}
