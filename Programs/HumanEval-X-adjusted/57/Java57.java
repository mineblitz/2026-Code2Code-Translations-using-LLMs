import java.util.*;
import java.lang.*;

public class Solution {
    public boolean monotonic(List<Integer> l) {
        List<Integer> l1 = new ArrayList<>(l), l2 = new ArrayList<>(l);
        Collections.sort(l1);
        l2.sort(Collections.reverseOrder());
        return l.equals(l1) || l.equals(l2);
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
    boolean result = solution.monotonic(n);
    System.out.println(result);
    }
}
