import java.util.*;
import java.lang.*;

public class Solution {
    public String exchange(List<Integer> lst1, List<Integer> lst2) {
        int odd = 0, even = 0;
        for (int i : lst1) {
            if (i % 2 == 1) {
                odd += 1;
            }
        }
        for (int i : lst2) {
            if (i % 2 == 0) {
                even += 1;
            }
        }
        if (even >= odd) {
            return "YES";
        }
        return "NO";
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
        String listString1 = args[1];
        List<Integer> o = new ArrayList<>();
        if (!listString1.equals("[]")) {
        listString1 = listString1.replace("[", "").replace("]", "");
        String[] tempArray1 = listString1.split(",");
        for (String value : tempArray1) {
            o.add(Integer.parseInt(value.trim()));
        }
        }
    String result = solution.exchange(n, o);
    System.out.println(result);
    }
}
