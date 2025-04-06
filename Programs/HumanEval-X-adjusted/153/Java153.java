import java.util.*;
import java.lang.*;

public class Solution {
    public String StrongestExtension(String class_name, List<String> extensions) {
        String strong = extensions.get(0);
        int my_val = (int) (strong.chars().filter(Character::isUpperCase).count() - strong.chars().filter(Character::isLowerCase).count());
        for (String s : extensions) {
            int val = (int) (s.chars().filter(Character::isUpperCase).count() - s.chars().filter(Character::isLowerCase).count());
            if (val > my_val) {
                strong = s;
                my_val = val;
            }
        }
        return class_name + "." + strong;
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            String n = args[0];
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
    String result = solution.StrongestExtension(n, o);
    System.out.println(result);
    }
}
