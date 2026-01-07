//Check whether a given integer is single-digit, double-digit, or multi-digit. 

import java.util.Scanner;

public class Delta {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number: ");
        int number = sc.nextInt(); // 1 11 (111 1111...)
        int num = Math.abs(number);
        if (num / 10 < 1){
            System.out.println("Single Digit Number");
        }else if(num / 100 < 1){
            System.out.println("Double Digit Number");
        }else{
            System.out.println("Multi Digit Number");
        }

        sc.close();
    }
}
