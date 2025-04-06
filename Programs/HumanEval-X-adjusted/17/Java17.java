import java.util.*;
import java.lang.*;

public class Solution {
    public List<Integer> parseMusic(String string) {
        String[] notes = string.split(" ");
        List<Integer> result = new ArrayList<>();
        for (String s : notes) {
            switch (s) {
                case "o" -> result.add(4);
                case "o|" -> result.add(2);
                case ".|" -> result.add(1);
            }
        }
        return result;
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            String n = args[0];
    List<Integer> result = solution.parseMusic(n);
    System.out.println(result);
    }
}
