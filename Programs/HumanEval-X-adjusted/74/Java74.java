import java.util.*;
import java.lang.*;

public class Solution {
    public List<String> totalMatch(List<String> lst1, List<String> lst2) {
        int l1 = 0;
        for (String st : lst1) {
            l1 += st.length();
        }

        int l2 = 0;
        for (String st : lst2) {
            l2 += st.length();
        }

        if (l1 <= l2) {
            return lst1;
        } else {
            return lst2;
        }
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
        String listString1 = args[1];
        List<String> o = new ArrayList<>();
        listString1 = listString1.replace("\'", "");
        if (!listString1.equals("[]")) {
        listString1 = listString1.replace("[", "").replace("]", "");
        String[] tempArray1 = listString1.split(",");
        for (String value : tempArray1) {
            o.add(value.trim());
        }
        }
    List<String> result = solution.totalMatch(n, o);
        System.out.print("[");
        if(result.size() > 0){ System.out.print("'");}
        String print = String.join("', '", result);
        if (!print.equals("")){System.out.print(print);}
        if(result.size() > 0){ System.out.print("'");}
        System.out.println("]");
    }
}
