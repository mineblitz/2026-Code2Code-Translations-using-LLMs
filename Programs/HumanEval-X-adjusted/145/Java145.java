import java.util.*;
import java.lang.*;

public class Solution {
    public List<Integer> orderByPoints(List<Integer> nums) {
        List<Integer> result = new ArrayList<>(nums);
        result.sort((o1, o2) -> {
            int sum1 = 0;
            int sum2 = 0;

            for (int i = 0; i < String.valueOf(o1).length(); i++) {
                if (i != 0 || o1 >= 0) {
                    sum1 += (String.valueOf(o1).charAt(i) - '0' );
                    if (i == 1 && o1 < 0) {
                        sum1 = -sum1;
                    }
                }
            }
            for (int i = 0; i < String.valueOf(o2).length(); i++) {
                if (i != 0 || o2 >= 0) {
                    sum2 += (String.valueOf(o2).charAt(i) - '0' );
                    if (i == 1 && o2 < 0) {
                        sum2 = -sum2;
                    }
                }
            }
            return Integer.compare(sum1, sum2);
        });
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
    List<Integer> result = solution.orderByPoints(n);
    System.out.println(result);
    }
}
