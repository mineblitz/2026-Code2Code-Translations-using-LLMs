import java.util.*;
import java.lang.*;

public class Solution {
    public double triangleArea(double a, double b, double c) {
        if (a + b <= c || a + c <= b || b + c <= a) {
            return -1;
        }
        double s = (a + b + c) / 2;
        double area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
        area = (double) Math.round(area * 100) / 100;
        return area;
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            int n = Integer.parseInt(args[0]);
            int o = Integer.parseInt(args[1]);
            int p = Integer.parseInt(args[2]);
    double result = solution.triangleArea(n, o, p);
    System.out.println(result);
    }
}
