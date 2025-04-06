import java.util.*;
import java.lang.*;

public class Solution {
    public List<Integer> common(List<Integer> l1, List<Integer> l2) {
        Set<Integer> ret = new HashSet<>(l1);
        ret.retainAll(new HashSet<>(l2));
        List<Integer> result = new ArrayList<>(ret);
        Collections.sort(result);
        return result;
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
        String listString1 = args[1];
        List<Integer> o = new ArrayList<>();
        if (!listString1.equals("[]")) {
        listString1 = listString1.replace("[", "").replace("]", "");
        String[] tempArray1 = listString1.split(",");
        for (String value : tempArray1) {
            o.add(Integer.parseInt(value.trim()));
        }
        }
    List<Integer> result = solution.common(n, o);
    System.out.println(result);
    }
}
