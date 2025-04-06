import java.util.*;
import java.lang.*;

public class Solution {
    public int largestPrimeFactor(int n) {
        int largest = 1;
        for (int j = 2; j <= n; j++) {
            if (n % j == 0) {
                boolean is_prime = j >= 2;
                for (int i = 2; i < j - 1; i++) {
                    if (j % i == 0) {
                        is_prime = false;
                        break;
                    }
                }
                if (is_prime) {
                    largest = Math.max(largest, j);
                }
            }
        }
        return largest;
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            int n = Integer.parseInt(args[0]);
    int result = solution.largestPrimeFactor(n);
    System.out.println(result);
    }
}
