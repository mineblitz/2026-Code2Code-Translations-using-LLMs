import java.util.*;
import java.lang.*;

public class Solution {
    public int digits(int n) {
        int product = 1, odd_count = 0;
        for (char digit : String.valueOf(n).toCharArray()) {
            int int_digit = digit - '0';
            if (int_digit % 2 == 1) {
                product *= int_digit;
                odd_count += 1;
            }
        }
        if (odd_count == 0) {
            return 0;
        } else {
            return product;
        }
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            int n = Integer.parseInt(args[0]);
    int result = solution.digits(n);
    System.out.println(result);
    }
}
