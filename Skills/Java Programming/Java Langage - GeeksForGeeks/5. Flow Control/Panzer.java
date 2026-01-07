import java.util.*;
public class Panzer {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        int ans = Math.max(a,b);
        ans = Math.max(c,ans);
        System.out.println(ans);
        sc.close();
    }
}
