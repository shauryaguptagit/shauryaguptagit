//Take a 3-digit number and check if all digits are distinct.

/*
 * 234
 * 4
 * 3
 * 2
 */

import java.util.Scanner;

public class Asset{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a three digit number: ");
        int threeDigitNum = sc.nextInt();

        int num1 = threeDigitNum % 10;
        int num2 = (threeDigitNum/10) % 10;
        int num3 = (threeDigitNum/100) % 10;

        if (num1 != num2 && num1 != num3 && num2 != num3){
            System.out.println("All are Distinct!");
        }else{
            System.out.println("Not Distinct!");
        }
        sc.close();
    }
}