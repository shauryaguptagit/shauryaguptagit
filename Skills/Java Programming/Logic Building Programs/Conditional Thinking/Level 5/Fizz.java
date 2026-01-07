//Take three numbers and check if they are in geometric progression.

//b^2 = a * c

import java.util.Scanner;

public class Fizz {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter num1: ");
        int x = sc.nextInt(); //8
        System.out.println("Enter num2: ");
        int y = sc.nextInt(); // 6
        System.out.println("Enter num3: ");
        int z = sc.nextInt(); // 5

        if ( x*x == y*z || y*y == x*z ||z*z == x*y ){
            System.out.println("In GP");
        }else{
            System.out.println("Not In GP");
        }
        sc.close();
    }
}
