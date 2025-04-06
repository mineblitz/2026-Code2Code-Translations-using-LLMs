import java.util.*;
import java.lang.*;

public class Solution {
    public boolean isNested(String string) {
        List<Integer> opening_bracket_index = new ArrayList<>(), closing_bracket_index = new ArrayList<>();
        for (int i = 0; i < string.length(); i++) {
            if (string.charAt(i) == '[') {
                opening_bracket_index.add(i);
            } else {
                closing_bracket_index.add(i);
            }
        }
        Collections.reverse(closing_bracket_index);
        int i = 0, l = closing_bracket_index.size();
        for (int idx : opening_bracket_index) {
            if (i < l && idx < closing_bracket_index.get(i)) {
                i += 1;
            }
        }
        return i >= 2;
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            String n = args[0];
    boolean result = solution.isNested(n);
    System.out.println(result);
    }
}
