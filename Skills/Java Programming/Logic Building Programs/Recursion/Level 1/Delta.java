//Print only odd numbers from 1 to n recursively. 

import java.util.Scanner;

public class Delta {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number (n): ");
        int n = sc.nextInt();

        System.out.println("Odd Numbers from 1 to " + n + ":");
        printOddNumbers(n);
        
        System.out.println(); // For a clean new line
        sc.close();
    }

    public static void printOddNumbers(int n){

        if (n <= 0) {
            return;
        }

        printOddNumbers(n - 1);

        if (n % 2 != 0) {
            System.out.print( n + " ");
        }

    }
}