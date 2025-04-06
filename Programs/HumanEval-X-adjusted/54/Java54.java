import java.util.*;
import java.lang.*;

public class Solution {
    public boolean sameChars(String s0, String s1) {
        Set<Character> set0 = new HashSet<>();
        for (char c : s0.toCharArray()) {
            set0.add(c);
        }
        Set<Character> set1 = new HashSet<>();
        for (char c : s1.toCharArray()) {
            set1.add(c);
        }
        return set0.equals(set1);
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            String n = args[0];
            String o = args[1];
    boolean result = solution.sameChars(n, o);
    System.out.println(result);
    }
}
