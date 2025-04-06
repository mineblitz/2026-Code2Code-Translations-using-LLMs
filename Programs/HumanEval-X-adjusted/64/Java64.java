import java.util.*;
import java.lang.*;

public class Solution {
    public int vowelsCount(String s) {
        String vowels = "aeiouAEIOU";
        int n_vowels = 0;
        for (char c : s.toCharArray()) {
            if (vowels.indexOf(c) != -1) {
                n_vowels += 1;
            }
        }
        if (s.charAt(s.length() - 1) == 'y' || s.charAt(s.length() - 1) == 'Y') {
            n_vowels += 1;
        }
        return n_vowels;
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            String n = args[0];
    int result = solution.vowelsCount(n);
    System.out.println(result);
    }
}
