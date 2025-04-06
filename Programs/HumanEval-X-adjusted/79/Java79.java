import java.util.*;
import java.lang.*;

public class Solution {
    public String decimalToBinary(int decimal) {
        return "db" + Integer.toBinaryString(decimal) + "db";
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            int n = Integer.parseInt(args[0]);
    String result = solution.decimalToBinary(n);
    System.out.println(result);
    }
}
