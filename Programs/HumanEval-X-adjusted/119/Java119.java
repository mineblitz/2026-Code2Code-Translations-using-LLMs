import java.util.*;
import java.lang.*;

public class Solution {
    public String matchParens(List<String> lst) {
        List<String> S = Arrays.asList(lst.get(0) + lst.get(1), lst.get(1) + lst.get(0));
        for (String s : S) {
            int val = 0;
            for (char i : s.toCharArray()) {
                if (i == '(') {
                    val += 1;
                } else {
                    val -= 1;
                }
                if (val < 0) {
                    break;
                }
            }
            if (val == 0) {
                return "Yes";
            }
        }
        return "No";
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
        String listString0 = args[0];
        List<String> n = new ArrayList<>();
        listString0 = listString0.replace("\'", "");
        if (!listString0.equals("[]")) {
        listString0 = listString0.replace("[", "").replace("]", "");
        String[] tempArray0 = listString0.split(",");
        for (String value : tempArray0) {
            n.add(value.trim());
        }
        }
    String result = solution.matchParens(n);
    System.out.println(result);
    }
}
