import java.util.*;
import java.lang.*;

public class Solution {
    public int canArrange(List<Integer> arr) {
        int ind = -1, i = 1;
        while (i < arr.size()) {
            if (arr.get(i) < arr.get(i - 1)) {
                ind = i;
            }
            i += 1;
        }
        return ind;
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
        String listString0 = args[0];
        List<Integer> n = new ArrayList<>();
        if (!listString0.equals("[]")) {
        listString0 = listString0.replace("[", "").replace("]", "");
        String[] tempArray0 = listString0.split(",");
        for (String value : tempArray0) {
            n.add(Integer.parseInt(value.trim()));
        }
        }
    int result = solution.canArrange(n);
    System.out.println(result);
    }
}
