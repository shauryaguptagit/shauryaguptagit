//Take two angles of a triangle and compute the third angle.

import java.util.Scanner;

public class Icicle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter angleOne: ");
        int angleOne = sc.nextInt();
        System.out.println("Enter angleTwo: ");
        int angleTwo = sc.nextInt();
        int thirdAngle = 0;

        if (angleOne <= 0 || angleTwo <= 0){
            System.out.println("Invalid Angles!");
        }else if(angleOne + angleTwo >= 180){
            System.out.println("Not a valid Triangle!");
        }else{
            thirdAngle = 180 - (angleOne + angleTwo);
            System.out.println("The third angle is: " + thirdAngle);
        }
        sc.close();
    }
}
