//Take an integer (1–9999) and check if the sum of its digits is greater than the product of its digits.


import java.util.Scanner;

public class Hector {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number: ");
        int num = sc.nextInt();
        
        int firstDigit;
        int secondDigit;
        int thirdDigit;
        int fouthDigit;



        if (num < 1 || num > 10000){
            System.out.println("Range should be 1-9999");
        }else if (num < 10){
            System.out.println("The sum of its digits is not greater than the product of its digits. ");
        }else if(num < 100){
            firstDigit = num % 10;
            secondDigit = num / 10;
            if (firstDigit + secondDigit > firstDigit * secondDigit){
                System.out.println("yes");
            }else{
                System.out.println("no");
            }
        }else if(num < 1000){
            firstDigit = num % 10;
            secondDigit = (num / 10) % 10;
            thirdDigit = num /100;
            if (firstDigit + secondDigit + thirdDigit > firstDigit * secondDigit * thirdDigit){
                System.out.println("yes");
            }else{
                System.out.println("no");
            }
        }else{
            firstDigit = num % 10; // 9999
            secondDigit = (num / 10) % 10;
            thirdDigit = (num /100) % 10;
            fouthDigit = num / 1000;
            if (firstDigit + secondDigit + thirdDigit + fouthDigit > firstDigit * secondDigit * thirdDigit * fouthDigit){
                System.out.println("yes");
            }else{
                System.out.println("no");
            }
        }
        sc.close();
    }
}
