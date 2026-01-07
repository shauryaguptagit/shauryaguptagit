import java.util.*;
public class FirstDigit {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(firstDigit(n));
        sc.close();
    }

    public static int firstDigit (int n){
    double power = Math.log10(n);
    int p = (int) power;
    double a = Math.pow(10,p);
    int ne = (int) a;
    int ans = n/ne;
    return ans;
    }
}

