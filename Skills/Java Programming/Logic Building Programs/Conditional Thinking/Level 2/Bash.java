//If the sides form a valid triangle, determine whether it is equilateral, isosceles, or scalene. 

import java.util.Scanner;

public class Bash {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter first side: ");
        int side1 = sc.nextInt();
        System.out.println("Enter second side: ");
        int side2 = sc.nextInt();
        System.out.println("Enter third side: ");
        int side3 = sc.nextInt();

        if (side1 == side2 && side1 == side3){
            System.out.println("Equilateral");
        }else if(side1 == side2  || side3 == side2  || side1 == side3){
            System.out.println("Isosceles");
        }else{
            System.out.println("Scalene");
        }
        sc.close();
    }    
}
