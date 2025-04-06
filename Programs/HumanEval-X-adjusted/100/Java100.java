import java.util.*;
import java.lang.*;

public class Solution {
    public List<Integer> makeAPile(int n) {
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            result.add(n + 2 * i);
        }
        return result;
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            int n = Integer.parseInt(args[0]);
    List<Integer> result = solution.makeAPile(n);
    System.out.println(result);
    }
}
