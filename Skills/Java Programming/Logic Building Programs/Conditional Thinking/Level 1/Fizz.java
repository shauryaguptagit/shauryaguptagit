//Take two numbers and print the larger one.

import java.util.Scanner;

public class Fizz {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter first number: ");
        int num1 = sc.nextInt();
        System.out.println("Enter second number: ");
        int num2 = sc.nextInt();
        if (num1>num2){
            System.out.println("Larger number is " + num1);
        }else{
            System.out.println("Larger number is " + num2);
        }
        sc.close();
    }
}
