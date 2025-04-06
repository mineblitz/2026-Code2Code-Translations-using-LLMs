import java.util.*;
import java.lang.*;

public class Solution {
    public int strlen(String string) {
        return string.length();
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            String n = args[0];
    int result = solution.strlen(n);
    System.out.println(result);
    }
}
