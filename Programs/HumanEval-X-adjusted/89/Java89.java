import java.util.*;
import java.lang.*;

public class Solution {
    public String encrypt(String s) {
        StringBuilder sb = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (Character.isLetter(c)) {
                sb.append((char) ('a' + (c - 'a' + 2 * 2) % 26));
            } else {
                sb.append(c);
            }
        }
        return sb.toString();
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            String n = args[0];
    String result = solution.encrypt(n);
    System.out.println(result);
    }
}
