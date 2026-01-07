//Back-end complete function Template for Java
import java.util.*;

public class Prime {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        boolean ans = true;
        if (n <= 1) {
            ans = false;
        }
        for (int i = 2; i < n; i++)
            if (n % i == 0) ans = false;

        if (ans == true) {
            System.out.println("True");
        } else {
            System.out.println("False");
        }
        sc.close();
    }
}