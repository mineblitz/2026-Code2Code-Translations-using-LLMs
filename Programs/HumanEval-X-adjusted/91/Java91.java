import java.util.*;
import java.lang.*;

public class Solution {
    public int isBored(String S) {
        String [] sentences = S.split("[.?!]\s*");
        int count = 0;
        for (String sentence : sentences) {
            if (sentence.subSequence(0, 2).equals("I ")) {
                count += 1;
            }
        }
        return count;
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            String n = args[0];
    int result = solution.isBored(n);
    System.out.println(result);
    }
}
