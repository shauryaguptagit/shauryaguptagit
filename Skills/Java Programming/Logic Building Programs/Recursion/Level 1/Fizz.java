//Print factorial of a number recursively.


import java.util.Scanner;

public class Fizz {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the term: ");
        int n = sc.nextInt();
        System.out.println("Factorial of " + n + " number is");
        int fact = factorial(n);
        System.out.println(fact);

        sc.close();
    }
    public static int factorial(int n){
        if (n <= 0) {
            return 1;
        }
        return n * factorial( n - 1 );
    }
}