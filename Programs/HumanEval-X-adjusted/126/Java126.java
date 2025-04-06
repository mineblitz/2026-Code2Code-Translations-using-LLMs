import java.util.*;
import java.lang.*;

public class Solution {
    public boolean isSorted(List<Integer> lst) {
        List<Integer> sorted_lst = new ArrayList<>(lst);
        Collections.sort(sorted_lst);
        if (!lst.equals(sorted_lst)) {
            return false;
        }
        for (int i = 0; i < lst.size() - 2; i++) {
            if (lst.get(i) == lst.get(i + 1) && lst.get(i) == lst.get(i + 2)) {
                return false;
            }
        }
        return true;
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
    boolean result = solution.isSorted(n);
    System.out.println(result);
    }
}
