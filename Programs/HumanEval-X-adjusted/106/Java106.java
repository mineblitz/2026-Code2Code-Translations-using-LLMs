import java.util.*;
import java.lang.*;

public class Solution {
    public List<Integer> f(int n) {
        List<Integer> ret = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if (i % 2 == 0) {
                int x = 1;
                for (int j = 1; j <= i; j++) {
                    x *= j;
                }
                ret.add(x);
            } else {
                int x = 0;
                for (int j = 1; j <= i; j++) {
                    x += j;
                }
                ret.add(x);
            }
        }
        return ret;
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            int n = Integer.parseInt(args[0]);
    List<Integer> result = solution.f(n);
    System.out.println(result);
    }
}
