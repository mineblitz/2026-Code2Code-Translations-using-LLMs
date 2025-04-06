import java.util.*;
import java.lang.*;

public class Solution {
    public List<Integer> sortArray(List<Integer> arr) {
                List < Integer > sorted_arr = new ArrayList<>(arr);
        sorted_arr.sort(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                int cnt1 = (int) Integer.toBinaryString(Math.abs(o1)).chars().filter(ch -> ch == '1').count();
                int cnt2 = (int) Integer.toBinaryString(Math.abs(o2)).chars().filter(ch -> ch == '1').count();
                if (cnt1 > cnt2) {
                    return 1;
                } else if (cnt1 < cnt2) {
                    return -1;
                } else {
                    return o1.compareTo(o2);
                }
            }
        });
        return sorted_arr;
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
    List<Integer> result = solution.sortArray(n);
    System.out.println(result);
    }
}
