import java.util.*;
import java.lang.*;

public class Solution {
    public int modp(int n, int p) {
        int ret = 1;
        for (int i = 0; i < n; i++) {
            ret = (ret * 2) % p;
        }
        return ret;
    }
    public static void main(String[] args) {
    Solution solution = new Solution();
            int n = Integer.parseInt(args[0]);
            int o = Integer.parseInt(args[1]);
    int result = solution.modp(n, o);
    System.out.println(result);
    }
}
