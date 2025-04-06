import java.util.*;
import java.lang.*;

public class Solution {
    public List<Integer> maximum(List<Integer> arr, int k) {
        if (k == 0) {
            return List.of();
        }
        List<Integer> arr_sort = new ArrayList<>(arr);
        Collections.sort(arr_sort);
        return arr_sort.subList(arr_sort.size() - k, arr_sort.size());
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
            int o = Integer.parseInt(args[1]);
    List<Integer> result = solution.maximum(n, o);
    System.out.println(result);
    }
}
