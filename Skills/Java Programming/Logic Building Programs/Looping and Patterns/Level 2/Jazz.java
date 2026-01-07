//Print sum of first n terms of Fibonacci series.

import java.util.Scanner;

public class Jazz {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter which number: "); // 0 1 1 2 3 5 8...
        int num = sc.nextInt();
        
        int firstDigit = 0;
        int secondDigit = 1;
        int countSum = 0;

        for( int i = 1; i <= num; i++){ // 0 1 2 3 4 5
            countSum += firstDigit;
            int nextDigit = firstDigit + secondDigit;
            firstDigit = secondDigit;
            secondDigit = nextDigit;
        }
        System.out.println(countSum);

        sc.close();
    }
}
