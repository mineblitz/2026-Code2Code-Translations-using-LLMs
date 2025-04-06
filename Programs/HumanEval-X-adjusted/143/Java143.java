import java.util.*;
import java.lang.*;

public class Solution {
    public String wordsInSentence(String sentence) {
        List<String> new_lst = new ArrayList<>();
        for (String word : sentence.split(" " )) {
            boolean flg = true;
            if (word.length() == 1) {
                continue;
            }
            for (int i = 2; i < word.length(); i++) {
                if (word.length() % i == 0) {
                    flg = false;
                    break;
                }
            }
            if (flg) {
                new_lst.add(word);
            }
        }
        return String.join(" ", new_lst);
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            String n = args[0];
    String result = solution.wordsInSentence(n);
    System.out.println(result);
    }
}
