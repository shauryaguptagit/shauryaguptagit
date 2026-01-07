//Take three numbers and check if they can form a Pythagorean triplet.

import java.util.Scanner;

public class Bash {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter 1 number: ");
        int num1 = sc.nextInt();
        System.out.println("Enter 2 number: ");
        int num2 = sc.nextInt();
        System.out.println("Enter 3 number: ");
        int num3 = sc.nextInt();
        
        if ( (num1*num1 + num2*num2 == num3*num3) || (num1*num1 == num2*num2 + num3*num3) || (num1*num1 + num3*num3 == num2*num2)){
            System.out.println("They form a Pythagorean Triplet " + num1 + num2 + num3 );
        } else{
            System.out.println("They do not form a Pythagorean Triplet" + num1 + num2 + num3 );
        }

        sc.close();
    }    
}
