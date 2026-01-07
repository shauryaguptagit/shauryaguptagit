//Take income and age, and check if eligible for tax (age > 18 and income > 5 L). 

import java.util.Scanner;

public class Ecta {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter your income (in Lacs): ");
        int income = sc.nextInt();
        System.out.println("Enter your age: ");
        int age = sc.nextInt();

        if (age > 18 && income > 5){
            System.out.println("Eligible for tax");
        }else{
            System.out.println("Not Eligible for tax");
        }
        sc.close();
    }
}
