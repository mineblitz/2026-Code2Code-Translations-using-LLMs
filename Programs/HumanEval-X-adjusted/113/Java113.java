import java.util.*;
import java.lang.*;

public class Solution {
    public List<String> oddCount(List<String> lst) {
        List<String> res = new ArrayList<>();
        for (String arr : lst) {
            int n = 0;
            for (char d : arr.toCharArray()) {
                if ((d - '0') % 2 == 1) {
                    n += 1;
                }
            }
            res.add("the number of odd elements " + n + "n the str" + n + "ng " + n + " of the " + n + "nput." );
        }
        return res;
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
    List<String> result = solution.oddCount(n);
        System.out.print("[");
        if(result.size() > 0){ System.out.print("'");}
        String print = String.join("', '", result);
        if (!print.equals("")){System.out.print(print);}
        if(result.size() > 0){ System.out.print("'");}
        System.out.println("]");
    }
}
