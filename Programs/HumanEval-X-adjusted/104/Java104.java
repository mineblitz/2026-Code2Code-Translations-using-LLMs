import java.util.*;
import java.lang.*;

public class Solution {
    public List<Integer> uniqueDigits(List<Integer> x) {
        List<Integer> odd_digit_elements = new ArrayList<>();
        for (int i : x) {
            boolean is_unique = true;
            for (char c : String.valueOf(i).toCharArray()) {
                if ((c - '0') % 2 == 0) {
                    is_unique = false;
                    break;
                }
            }
            if (is_unique) {
                odd_digit_elements.add(i);
            }
        }
        Collections.sort(odd_digit_elements);
        return odd_digit_elements;
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
    List<Integer> result = solution.uniqueDigits(n);
    System.out.println(result);
    }
}
