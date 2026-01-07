//Print only even numbers from 1 to n recursively. 

import java.util.Scanner;

public class Czech {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number (n): ");
        int n = sc.nextInt();

        System.out.println("Even Numbers from 1 to " + n + ":");
        printEvenNumbers(n);
        
        System.out.println(); // For a clean new line
        sc.close();
    }

    public static void printEvenNumbers(int n){

        if (n <= 0) {
            return;
        }

        printEvenNumbers(n - 1);

        if (n % 2 == 0) {
            System.out.print( n + " ");
        }

    }
}
