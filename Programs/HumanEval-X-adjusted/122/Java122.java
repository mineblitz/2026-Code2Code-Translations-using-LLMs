import java.util.*;
import java.lang.*;

public class Solution {
    public int addElements(List<Integer> arr, int k) {
        arr = arr.subList(0, k);
        Optional<Integer> sum = arr.stream().filter(p -> String.valueOf(Math.abs(p)).length() <= 2).reduce(Integer::sum);
        return sum.orElse(0);
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
    int result = solution.addElements(n, o);
    System.out.println(result);
    }
}
