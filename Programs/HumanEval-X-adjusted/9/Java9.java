import java.util.*;
import java.lang.*;

public class Solution {
    public List<Integer> rollingMax(List<Integer> numbers) {
        List<Integer> result = new ArrayList<>();
        if (numbers.size() == 0) {
            return result;
        }
        int rollingMax = numbers.get(0);
        result.add(rollingMax);

        for (int i = 1; i < numbers.size(); i++) {
            if (numbers.get(i) > rollingMax) {
                rollingMax = numbers.get(i);
            }
            result.add(rollingMax);
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
    List<Integer> result = solution.rollingMax(n);
    System.out.println(result);
    }
}
