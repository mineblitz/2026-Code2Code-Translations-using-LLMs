import java.util.*;
import java.lang.*;

public class Solution {
    public int howManyTimes(String string, String substring) {
        int times = 0;

        for (int i = 0; i < string.length() - substring.length() + 1; i++) {
            if (string.substring(i, i + substring.length()).equals(substring)) {
                times += 1;
            }
        }

        return times;
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            String n = args[0];
            String o = args[1];
    int result = solution.howManyTimes(n, o);
    System.out.println(result);
    }
}
