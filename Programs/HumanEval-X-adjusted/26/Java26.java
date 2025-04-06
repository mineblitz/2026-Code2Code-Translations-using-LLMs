import java.util.*;
import java.lang.*;
import java.util.stream.Collectors;

public class Solution {
    public List<Integer> removeDuplicates(List<Integer> numbers) {
        Map<Integer, Integer> c = new HashMap<>();
        for (int i : numbers) {
            c.put(i, c.getOrDefault(i, 0) + 1);
        }
        return numbers.stream().filter(i -> c.get(i) == 1).collect(Collectors.toList());
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
    List<Integer> result = solution.removeDuplicates(n);
    System.out.println(result);
    }
}
