//Calculate power of a number (xⁿ) using recursion.

import java.util.Scanner;

public class Growl {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the base (x): ");
        double x = sc.nextDouble();
        System.out.println("Enter the exponent (n): ");
        int n = sc.nextInt();

        double result = power(x, n);
        System.out.println(x + " raised to the power " + n + " is: " + result);

        sc.close();
    }
    public static double power(double x, int n){
        if (n == 0) {
            return 1.0;
        }
        
        // 2. Handle Negative Exponent: 5^-3 is 1 / (5^3)
        else if (n < 0) {
            return 1.0 / power(x, -n);
        }
        
        // 3. Recursive Step (for n > 0): 5^3 is 5 * 5^2
        else {
            return x * power(x, n - 1);
        }
    }
}
