import java.util.*;
public class GP {
    
    public static int NthTerm(int a, int r, int n){
        int ans = a* (int)(Math.pow(r,n-1));
        return ans;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int r = sc.nextInt();
        int n = sc.nextInt();
        System.out.println(NthTerm(a,r,n));
        sc.close();
    }
}
