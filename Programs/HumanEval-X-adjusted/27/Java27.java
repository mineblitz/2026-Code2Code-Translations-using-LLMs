import java.util.*;
import java.lang.*;

public class Solution {
    public String flipCase(String string) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < string.length(); i++) {
            if (Character.isLowerCase(string.charAt(i))) {
                sb.append(Character.toUpperCase(string.charAt(i)));
            } else {
                sb.append(Character.toLowerCase(string.charAt(i)));
            }
        }
        return sb.toString();
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            String n = args[0];
    String result = solution.flipCase(n);
    System.out.println(result);
    }
}
