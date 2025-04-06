import java.util.*;
import java.lang.*;

public class Solution {
    public boolean isEqualToSumEven(int n) {
        return n % 2 == 0 && n >= 8;
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            int n = Integer.parseInt(args[0]);
    boolean result = solution.isEqualToSumEven(n);
    System.out.println(result);
    }
}
