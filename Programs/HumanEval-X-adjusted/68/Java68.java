import java.util.*;
import java.lang.*;

public class Solution {
    public List<Integer> pluck(List<Integer> arr) {
        List<Integer> result = new ArrayList<>();
        if (arr.size() == 0) {
            return result;
        }
        int min = Integer.MAX_VALUE;
        int minIndex = -1;
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) % 2 == 0) {
                if (arr.get(i) < min) {
                    min = arr.get(i);
                    minIndex = i;
                }
            }
        }
        if (minIndex != -1) {
            result.add(min);
            result.add(minIndex);
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
    List<Integer> result = solution.pluck(n);
    System.out.println(result);
    }
}
