//Find nth Fibonacci number recursively

import java.util.Scanner;

public class Hector {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number (n): ");
        int n = sc.nextInt();

        // Use 'long' because Fibonacci numbers get very large, very fast
        long result = fibonacci(n);
        System.out.println("The " + n + "th Fibonacci number is: " + result);
        
        sc.close();
    }
    public static long fibonacci(int n){
        if (n == 0) {
            return 0;
        }

        if (n == 1) {
            return 1;
        }

        return fibonacci(n - 1) + fibonacci(n - 2);
        
    }
}
