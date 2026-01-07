import java.util.*;
public class AP {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int n = sc.nextInt();
        int d = sc.nextInt();
        int term = a + (n-1)*d;
        System.out.println(term);
        sc.close();
    }
}
