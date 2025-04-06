import java.util.*;
import java.lang.*;

public class Solution {
    public double triangleArea(double a, double h) {
        return a * h / 2;
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            int n = Integer.parseInt(args[0]);
            int o = Integer.parseInt(args[1]);
    double result = solution.triangleArea(n, o);
    System.out.println(result);
    }
}
