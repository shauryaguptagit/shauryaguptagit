//Print numbers from n down to 1 using recursion.

import java.util.Scanner;

public class Bash {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number: ");
        int n = sc.nextInt();

        System.out.println("Numbers from " + n + " to 1:");
        printNumbers(n);

        System.out.println();
        sc.close();
    }

    public static void printNumbers(int n){
        if ( n <= 0){
            return;
        }
        System.out.print( n + " ");
        printNumbers(n - 1);

    }
}
