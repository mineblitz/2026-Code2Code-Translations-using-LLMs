import java.util.*;
import java.lang.*;

public class Solution {
    public int fib4(int n) {
        List<Integer> results = new ArrayList<>();
        results.add(0);
        results.add(0);
        results.add(2);
        results.add(0);
        if (n < 4) {
            return results.get(n);
        }

        for (int i = 4; i <= n; i++) {
            results.add(results.get(0) + results.get(1) + results.get(2) + results.get(3));
            results.remove(0);
        }
        return results.get(3);
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            int n = Integer.parseInt(args[0]);
    int result = solution.fib4(n);
    System.out.println(result);
    }
}
