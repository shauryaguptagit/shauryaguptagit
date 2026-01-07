//Print the sum of all odd digits and even digits separately in a number. 


import java.util.Scanner;

public class Icicle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number: ");
        int num = sc.nextInt(); //5467

        int sumEvenDigit = 0;
        int sumOddDigit = 0;
        int tempNum = num;

        while( tempNum > 0 ){
            int digit = tempNum % 10;
            
            if( digit % 2 == 0 ){
                sumEvenDigit += digit;
            }else{
                sumOddDigit += digit;
            }
            tempNum /= 10;
        }
        System.out.println("Sum of Odd Digits " + sumOddDigit);
        System.out.println("Sum of Even Digits " + sumEvenDigit);

        sc.close();
    }
}
