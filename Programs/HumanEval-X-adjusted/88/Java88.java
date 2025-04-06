import java.util.*;
import java.lang.*;

public class Solution {
    public List<Integer> sortArray(List<Integer> array) {
        if (array.size() == 0) {
            return array;
        }
        List<Integer> result = new ArrayList<>(array);
        if ((result.get(0) + result.get(result.size() - 1)) % 2 == 1) {
            Collections.sort(result);
        } else {
            result.sort(Collections.reverseOrder());
        }
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
    List<Integer> result = solution.sortArray(n);
    System.out.println(result);
    }
}
