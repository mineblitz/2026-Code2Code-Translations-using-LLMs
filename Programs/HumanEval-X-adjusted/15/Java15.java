import java.util.*;
import java.lang.*;

public class Solution {
    public String stringSequence(int n) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(i);
            sb.append(" ");
        }
        sb.append(n);
        return sb.toString();
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            int n = Integer.parseInt(args[0]);
    String result = solution.stringSequence(n);
    System.out.println(result);
    }
}
