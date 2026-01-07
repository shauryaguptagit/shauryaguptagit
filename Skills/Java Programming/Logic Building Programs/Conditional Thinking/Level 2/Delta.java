//Check if one of two given numbers is a multiple of the other.

import java.util.Scanner;

public class Delta {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter first number: ");
        int num1 = sc.nextInt();
        System.out.println("Enter second number: ");
        int num2 = sc.nextInt();
        
        if (num1 == 0 || num2 == 0){
            System.out.println("You cannot divide by Zero!");
        }else if(num1 % num2 == 0 || num2 % num1 == 0){
            System.out.println("Yes one of two given numbers is a multiple of the other");
        }else{
            System.out.println("No one of two given numbers is a multiple of the other");
        }
        sc.close();
    }
}
