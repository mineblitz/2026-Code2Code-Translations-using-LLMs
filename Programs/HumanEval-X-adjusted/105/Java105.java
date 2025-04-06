import java.util.*;
import java.lang.*;

public class Solution {
    public List<String> byLength(List<Integer> arr) {
        List<Integer> sorted_arr = new ArrayList<>(arr);
        sorted_arr.sort(Collections.reverseOrder());
        List<String> new_arr = new ArrayList<>();
        for (int var : sorted_arr) {
            if (var >= 1 && var <= 9) {
                switch (var) {
                    case 1 -> new_arr.add("One");
                    case 2 -> new_arr.add("Two");
                    case 3 -> new_arr.add("Three");
                    case 4 -> new_arr.add("Four");
                    case 5 -> new_arr.add("Five");
                    case 6 -> new_arr.add("Six");
                    case 7 -> new_arr.add("Seven");
                    case 8 -> new_arr.add("Eight");
                    case 9 -> new_arr.add("Nine");
                }
            }
        }
        return new_arr;
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
    List<String> result = solution.byLength(n);
        System.out.print("[");
        if(result.size() > 0){ System.out.print("'");}
        String print = String.join("', '", result);
        if (!print.equals("")){System.out.print(print);}
        if(result.size() > 0){ System.out.print("'");}
        System.out.println("]");
    }
}
