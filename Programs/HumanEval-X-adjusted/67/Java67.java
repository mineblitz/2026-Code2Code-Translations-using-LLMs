import java.util.*;
import java.lang.*;

public class Solution {
    public int fruitDistribution(String s, int n) {
        List<Integer> lis = new ArrayList<>();
        for (String i : s.split(" ")) {
            try {
                lis.add(Integer.parseInt(i));
            } catch (NumberFormatException ignored) {

            }
        }
        return n - lis.stream().mapToInt(Integer::intValue).sum();
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            String n = args[0];
            int o = Integer.parseInt(args[1]);
    int result = solution.fruitDistribution(n, o);
    System.out.println(result);
    }
}
