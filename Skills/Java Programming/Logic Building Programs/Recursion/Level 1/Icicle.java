// Print Fibonacci series up to n terms recursively.

import java.util.Scanner;

public class Icicle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("How many terms of the Fibonacci series do you want?");
        int n = sc.nextInt();

        System.out.println("Fibonacci series up to " + n + " terms:");
        
        // Start the recursion.
        // We start 'count' at 1 because we are about to print the 1st term.
        printFibonacci(0, 1, 1, n); 
        
        System.out.println(); // For a clean new line
        sc.close();
    }

    public static void printFibonacci(long a, long b, int count, int n) {
        
        // 1. Base Case: We've printed all the terms we need.
        if (count > n) {
            return;
        }
        
        // 2. Work: Print the current term.
        System.out.print(a + " ");
        
        // 3. Recursive Step: Call for the next term.
        // 'a' becomes 'b', 'b' becomes 'a + b', and we increment the count.
        printFibonacci(b, a + b, count + 1, n);
    }
}
