import java.util.*;
import java.lang.*;

public class Solution {
    public double meanAbsoluteDeviation(List<Double> numbers) {
        double sum = 0.0;
        for (double num : numbers) {
            sum += num;
        }
        double mean = sum / numbers.size();
        double sum_abs_diff = 0.0;
        for (double num : numbers) {
            sum_abs_diff += Math.abs(num - mean);
        }
        return sum_abs_diff / numbers.size();
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
        String listString0 = args[0];
        List<Double> n = new ArrayList<>();
        if (!listString0.equals("[]")) {
        listString0 = listString0.replace("[", "").replace("]", "");
        String[] tempArray0 = listString0.split(",");
        for (String value : tempArray0) {
            n.add(Double.parseDouble(value.trim()));
        }
        }
    double result = solution.meanAbsoluteDeviation(n);
    System.out.println(result);
    }
}
