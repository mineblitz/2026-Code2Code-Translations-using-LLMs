import java.util.*;
import java.lang.*;

public class Solution {
    public boolean checkIfLastCharIsALetter(String txt) {
        String[] words = txt.split(" ", -1);
        String check = words[words.length - 1];
        return check.length() == 1 && Character.isLetter(check.charAt(0));
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            String n = args[0];
    boolean result = solution.checkIfLastCharIsALetter(n);
    System.out.println(result);
    }
}
