import java.util.*;
import java.lang.*;

public class Solution {
    public int sumToN(int n) {
        int result = 0;
        for (int i = 1; i <= n; i++) {
            result += i;
        }
        return result;
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            int n = Integer.parseInt(args[0]);
    int result = solution.sumToN(n);
    System.out.println(result);
    }
}
