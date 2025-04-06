import java.util.*;
import java.lang.*;

public class Solution {
    public int sumSquares(List<Double> lst) {
        return lst.stream().map(p -> (int) Math.ceil(p)).map(p -> p * p).reduce(Integer::sum).get();
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
    int result = solution.sumSquares(n);
    System.out.println(result);
    }
}
