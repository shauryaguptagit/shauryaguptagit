//Take three sides and check if they form a valid triangle.

import java.util.Scanner;

public class Asset{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter first side: ");
        int side1 = sc.nextInt();
        System.out.println("Enter second side: ");
        int side2 = sc.nextInt();
        System.out.println("Enter third side: ");
        int side3 = sc.nextInt();
        if(side1+side2>side3 && side3+side2>side1 && side1+side3>side2){
            System.out.println("Triangle!");
        }else{
            System.out.println("Not a Triangle!");
        }
        sc.close();
    }
}