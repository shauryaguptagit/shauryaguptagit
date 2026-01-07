import java.util.*;
public class Last {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int real_num = Math.abs(num);
        int ans = real_num % 10;
        System.out.println(ans);
        sc.close();
    }
}
