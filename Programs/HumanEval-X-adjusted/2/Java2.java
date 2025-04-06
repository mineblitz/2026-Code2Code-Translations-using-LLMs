import java.util.*;
import java.lang.*;

public class Solution {
    public double truncateNumber(double number) {
        return number % 1.0;
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            double n = Float.parseFloat(args[0]);
    double result = solution.truncateNumber(n);
    System.out.println(result);
    }
}
