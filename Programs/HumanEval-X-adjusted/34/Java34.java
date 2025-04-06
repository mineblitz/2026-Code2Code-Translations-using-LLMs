import java.util.*;
import java.lang.*;

public class Solution {
    public List<Integer> unique(List<Integer> l) {
        List<Integer> result = new ArrayList<>(new HashSet<>(l));
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
    List<Integer> result = solution.unique(n);
    System.out.println(result);
    }
}
