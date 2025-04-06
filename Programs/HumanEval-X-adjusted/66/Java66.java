import java.util.*;
import java.lang.*;

public class Solution {
    public int digitSum(String s) {
        int sum = 0;
        for (char c : s.toCharArray()) {
            if (Character.isUpperCase(c)) {
                sum += c;
            }
        }
        return sum;
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            String n = args[0];
    int result = solution.digitSum(n);
    System.out.println(result);
    }
}
