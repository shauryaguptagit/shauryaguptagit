//Take three numbers and check if they are in arithmetic progression.

import java.util.Scanner;

public class Ecta {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter num1: ");
        int x = sc.nextInt();
        System.out.println("Enter num2: ");
        int y = sc.nextInt();
        System.out.println("Enter num3: ");
        int z = sc.nextInt();

        if ( 2*x == y + z || 2*y == x + z || 2*z == y + x ){
            System.out.println("In AP");
        }else{
            System.out.println("Not In AP");

        }
        sc.close();
    }
}
