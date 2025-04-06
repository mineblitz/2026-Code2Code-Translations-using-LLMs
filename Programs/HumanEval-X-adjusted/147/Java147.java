import java.util.*;
import java.lang.*;

public class Solution {
    public int getMaxTriples(int n) {
        List<Integer> A = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            A.add(i * i - i + 1);
        }
        int count = 0;
        for (int i = 0; i < A.size(); i++) {
            for (int j = i + 1; j < A.size(); j++) {
                for (int k = j + 1; k < A.size(); k++) {
                    if ((A.get(i) + A.get(j) + A.get(k)) % 3 == 0) {
                        count += 1;
                    }
                }
            }
        }
        return count;
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            int n = Integer.parseInt(args[0]);
    int result = solution.getMaxTriples(n);
    System.out.println(result);
    }
}
