//Print numbers from 1 to n using recursion.

import java.util.Scanner;

public class Asset{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number (n): ");
        int n = sc.nextInt();

        System.out.println("Numbers from 1 to " + n + ":");
        printNumbers(n);

        System.out.println(); // For a clean new line
        sc.close();
    }

    public static void printNumbers(int n){
        if (n <= 0){
            return;
        }

        printNumbers(n - 1);

        System.out.print(n + " ");
    }
}

