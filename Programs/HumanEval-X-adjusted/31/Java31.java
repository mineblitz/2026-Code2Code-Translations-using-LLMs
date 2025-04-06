import java.util.*;
import java.lang.*;

public class Solution {
    public boolean isPrime(int n) {
        if (n < 2) {
            return false;
        }
        for (int k = 2; k < n; k++) {
            if (n % k == 0) {
                return false;
            }
        }
         return true;
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            int n = Integer.parseInt(args[0]);
    boolean result = solution.isPrime(n);
    System.out.println(result);
    }
}
