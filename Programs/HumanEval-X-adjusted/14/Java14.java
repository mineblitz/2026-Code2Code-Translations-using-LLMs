import java.util.*;
import java.lang.*;

public class Solution {
    public List<String> allPrefixes(String string) {
        List<String> result = new ArrayList<>();

        for (int i = 1; i <= string.length(); i++) {
            result.add(string.substring(0, i));
        }
        return result;
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            String n = args[0];
    List<String> result = solution.allPrefixes(n);
        System.out.print("[");
        if(result.size() > 0){ System.out.print("'");}
        String print = String.join("', '", result);
        if (!print.equals("")){System.out.print(print);}
        if(result.size() > 0){ System.out.print("'");}
        System.out.println("]");
    }
}
