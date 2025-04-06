import java.util.*;
import java.lang.*;

public class Solution {
    public String antiShuffle(String s) {
        String[] strings = s.split(" ");
        List<String> result = new ArrayList<>();
        for (String string : strings) {
            char[] chars = string.toCharArray();
            Arrays.sort(chars);
            result.add(String.copyValueOf(chars));
        }
        return String.join(" ", result);
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            String n = args[0];
    String result = solution.antiShuffle(n);
    System.out.println(result);
    }
}
