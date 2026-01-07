//Find sum of digits of a number recursively. 

import java.util.Scanner;

public class Jazz {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number: ");
        int num = sc.nextInt();

        // Use Math.abs() to handle negative numbers gracefully
        int result = sumOfDigits(Math.abs(num));
        
        System.out.println("The sum of the digits is: " + result);
        
        sc.close();
    }

    public static int sumOfDigits(int num) {
        if (num == 0) {
            return 0;
        }
        
        return (num % 10) + sumOfDigits(num/10);
    }
}