import java.util.*;
import java.lang.*;
import java.util.stream.Collectors;

public class Solution {
    public List<Integer> getPositive(List<Integer> l) {
        return l.stream().filter(p -> p > 0).collect(Collectors.toList());
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
    List<Integer> result = solution.getPositive(n);
    System.out.println(result);
    }
}
