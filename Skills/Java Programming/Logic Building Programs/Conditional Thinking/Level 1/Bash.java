//Check if a number is even or odd.

import java.util.Scanner;

public class Bash {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number: ");
        double num = sc.nextDouble();
        if (num % 2 == 0) {
            System.out.println("Even!");
        }else{
            System.out.println("Odd!");
        }
        sc.close();
    }    
}
