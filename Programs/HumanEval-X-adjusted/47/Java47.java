import java.util.*;
import java.lang.*;

public class Solution {
    public double median(List<Integer> l) {
        List<Integer> list = l;
        Collections.sort(list);
        if (l.size() % 2 == 1) {
            return l.get(l.size() / 2);
        } else {
            return (l.get(l.size() / 2 - 1) + l.get(l.size() / 2)) / 2.0;
        }
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
    double result = solution.median(n);
    System.out.println(result);
    }
}
