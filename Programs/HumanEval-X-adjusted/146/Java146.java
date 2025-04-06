import java.util.*;
import java.lang.*;

public class Solution {
    public int specialFilter(List<Integer> nums) {
        int count = 0;
        for (int num : nums) {
            if (num > 10) {
                String odd_digits = "13579";
                String number_as_string = String.valueOf(num);
                if (odd_digits.indexOf(number_as_string.charAt(0)) != -1 && odd_digits.indexOf(number_as_string.charAt(number_as_string.length() - 1)) != -1) {
                    count += 1;
                }
            }
        }
        return count;
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
    int result = solution.specialFilter(n);
    System.out.println(result);
    }
}
