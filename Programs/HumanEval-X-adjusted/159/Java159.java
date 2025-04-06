import java.util.*;
import java.lang.*;

public class Solution {
    public List<Integer> eat(int number, int need, int remaining) {
        if (need <= remaining) {
            return Arrays.asList(number + need, remaining - need);
        } else {
            return Arrays.asList(number + remaining, 0);
        }
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            int n = Integer.parseInt(args[0]);
            int o = Integer.parseInt(args[1]);
            int p = Integer.parseInt(args[2]);
    List<Integer> result = solution.eat(n, o, p);
    System.out.println(result);
    }
}
