import java.util.*;
import java.lang.*;

public class Solution {
    public List<Double> rescaleToUnit(List<Double> numbers) {
        double min_number = Collections.min(numbers);
        double max_number = Collections.max(numbers);
        List<Double> result = new ArrayList<>();
        for (double x : numbers) {
            result.add((x - min_number) / (max_number - min_number));
        }
        return result;
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
    List<Double> result = solution.rescaleToUnit(n);
    System.out.println(result);
    }
}
