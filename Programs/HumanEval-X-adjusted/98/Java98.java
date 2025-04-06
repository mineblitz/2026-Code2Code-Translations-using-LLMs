import java.util.*;
import java.lang.*;

public class Solution {
    public int countUpper(String s) {
        int count = 0;
        for (int i = 0; i < s.length(); i += 2) {
            if ("AEIOU".indexOf(s.charAt(i)) != -1) {
                count += 1;
            }
        }
        return count;
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            String n = args[0];
    int result = solution.countUpper(n);
    System.out.println(result);
    }
}
