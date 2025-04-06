import java.util.*;
import java.lang.*;

public class Solution {
    public int countDistinctCharacters(String string) {
        Set<Character> set = new HashSet<>();
        for (char c : string.toLowerCase().toCharArray()) {
            set.add(c);
        }
        return set.size();
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            String n = args[0];
    int result = solution.countDistinctCharacters(n);
    System.out.println(result);
    }
}
