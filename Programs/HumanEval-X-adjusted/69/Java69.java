import java.util.*;
import java.lang.*;

public class Solution {
    public int search(List<Integer> lst) {
        int[] frq = new int[Collections.max(lst) + 1];
        for (int i : lst) {
            frq[i] += 1;
        }
        int ans = -1;
        for (int i = 1; i < frq.length; i++) {
            if (frq[i] >= i) {
                ans = i;
            }
        }
        return ans;
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
    int result = solution.search(n);
    System.out.println(result);
    }
}
