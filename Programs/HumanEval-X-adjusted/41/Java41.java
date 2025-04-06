import java.util.*;
import java.lang.*;

public class Solution {
    public int carRaceCollision(int n) {
        return n * n;
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            int n = Integer.parseInt(args[0]);
    int result = solution.carRaceCollision(n);
    System.out.println(result);
    }
}
