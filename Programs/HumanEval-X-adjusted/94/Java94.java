import java.util.*;
import java.lang.*;

public class Solution {
    public int skjkasdkd(List<Integer> lst) {
        int maxx = 0;
        for (int i : lst) {
            if (i > maxx) {
                boolean isPrime = i != 1;
                for (int j = 2; j < Math.sqrt(i) + 1; j++) {
                    if (i % j == 0) {
                        isPrime = false;
                        break;
                    }
                }
                if (isPrime) {
                    maxx = i;
                }
            }
        }
        int sum = 0;
        for (char c : String.valueOf(maxx).toCharArray()) {
            sum += (c - '0');
        }
        return sum;
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
    int result = solution.skjkasdkd(n);
    System.out.println(result);
    }
}
