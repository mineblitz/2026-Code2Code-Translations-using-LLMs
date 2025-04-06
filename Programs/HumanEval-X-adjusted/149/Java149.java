import java.util.*;
import java.lang.*;

public class Solution {
    public List<String> listSort(List<String> lst) {
        List<String> lst_sorted = new ArrayList<>(lst);
        Collections.sort(lst_sorted);
        List<String> new_lst = new ArrayList<>();
        for (String i : lst_sorted) {
            if (i.length() % 2 == 0) {
                new_lst.add(i);
            }
        }
        new_lst.sort(Comparator.comparingInt(String::length));
        return new_lst;
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
        String listString0 = args[0];
        List<String> n = new ArrayList<>();
        listString0 = listString0.replace("\'", "");
        if (!listString0.equals("[]")) {
        listString0 = listString0.replace("[", "").replace("]", "");
        String[] tempArray0 = listString0.split(",");
        for (String value : tempArray0) {
            n.add(value.trim());
        }
        }
    List<String> result = solution.listSort(n);
        System.out.print("[");
        if(result.size() > 0){ System.out.print("'");}
        String print = String.join("', '", result);
        if (!print.equals("")){System.out.print(print);}
        if(result.size() > 0){ System.out.print("'");}
        System.out.println("]");
    }
}
