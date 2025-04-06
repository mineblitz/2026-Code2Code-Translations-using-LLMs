import java.util.*;
import java.lang.*;

public class Solution {
    public String concatenate(List<String> strings) {
        return String.join("", strings);
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
    String result = solution.concatenate(n);
    System.out.println(result);
    }
}
