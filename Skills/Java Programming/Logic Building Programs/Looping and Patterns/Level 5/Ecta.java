// Find the smallest and largest digit in a given number. 

import java.util.Scanner;

public class Ecta {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number: ");
        int num = sc.nextInt(); // 10 100
        
        if ( num == 0){
            System.out.println("Largest digit: 0");
            System.out.println("Smallest digit: 0");
        } else {
            int tempNum = Math.abs(num);
            int maxDigit = 0;
            int minDigit = 9;

            while (tempNum > 0) {
                int digit = tempNum % 10;

                if (digit < minDigit){
                    minDigit = digit;
                }

                if (digit > maxDigit){
                    maxDigit = digit;
                }
                tempNum /= 10;
            }
            System.out.println("Largest digit: " + maxDigit);
            System.out.println("Smallest digit: " + minDigit);
        }
        
        sc.close();
    }
}