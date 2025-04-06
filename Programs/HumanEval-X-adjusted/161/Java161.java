import java.util.*;
import java.lang.*;

public class Solution {
    public String solve(String s) {
        boolean flag = true;
        StringBuilder new_string = new StringBuilder();
        for (char i : s.toCharArray()) {
            if (Character.isUpperCase(i)) {
                new_string.append(Character.toLowerCase(i));
                flag = false;
            } else if (Character.isLowerCase(i)) {
                new_string.append(Character.toUpperCase(i));
                flag = false;
            } else {
                new_string.append(i);
            }
        }
        if (flag) {
            new_string.reverse();
        }
        return new_string.toString();
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            String n = args[0];
    String result = solution.solve(n);
    System.out.println(result);
    }
}
