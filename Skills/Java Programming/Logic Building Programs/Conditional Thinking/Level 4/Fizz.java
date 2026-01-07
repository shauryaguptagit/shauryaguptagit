//Take two numbers and check if both are positive and their sum is less than 100.

import java.util.Scanner;

public class Fizz {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter abscissa: ");
        int x = sc.nextInt();
        System.out.println("Enter ordinate: ");
        int y = sc.nextInt();
        
        if ( x > 0 && y > 0 && x + y < 100){
            System.out.println("both are positive and their sum is less than 100");
        }else{
            System.out.println("both are not positive and their sum is not less than 100");
        }

        sc.close();
    }
}
