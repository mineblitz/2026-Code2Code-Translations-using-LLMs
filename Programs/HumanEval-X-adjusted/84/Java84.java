import java.util.*;
import java.lang.*;

public class Solution {
    public String solve(int N) {
        int sum = 0;
        for (char c : String.valueOf(N).toCharArray()) {
            sum += (c - '0');
        }
        return Integer.toBinaryString(sum);
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            int n = Integer.parseInt(args[0]);
    String result = solution.solve(n);
    System.out.println(result);
    }
}
