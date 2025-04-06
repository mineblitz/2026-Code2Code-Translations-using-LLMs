import java.util.*;
import java.lang.*;

public class Solution {
    public String stringXor(String a, String b) {
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) == b.charAt(i)) {
                result.append("0");
            } else {
                result.append("1");
            }
        }
        return result.toString();
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            String n = args[0];
            String o = args[1];
    String result = solution.stringXor(n, o);
    System.out.println(result);
    }
}
