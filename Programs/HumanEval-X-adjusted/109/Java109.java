import java.util.*;
import java.lang.*;

public class Solution {
    public boolean moveOneBall(List<Integer> arr) {
        if (arr.size() == 0) {
            return true;
        }
        List<Integer> sorted_arr = new ArrayList<>(arr);
        Collections.sort(sorted_arr);

        int min_value = Collections.min(arr);
        int min_index = arr.indexOf(min_value);
        List<Integer> my_arr = new ArrayList<>(arr.subList(min_index, arr.size()));
        my_arr.addAll(arr.subList(0, min_index));
        for (int i = 0; i < arr.size(); i++) {
            if (my_arr.get(i) != sorted_arr.get(i)) {
                return false;
            }
        }
        return true;
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
    boolean result = solution.moveOneBall(n);
    System.out.println(result);
    }
}
