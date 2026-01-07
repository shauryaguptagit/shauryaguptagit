//Take coordinates (x, y) and determine which quadrant the point lies in. 

import java.util.Scanner;

public class Fizz {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter abscissa: ");
        int x = sc.nextInt();
        System.out.println("Enter ordinate: ");
        int y = sc.nextInt();
        if (x == 0 || y == 0){
            if (x == 0 && y ==0){
                System.out.println("At Origin!");
            }else{
                System.out.println("At Axis!");
            }
        }else if ( x > 0){
            if (y > 0){
                System.out.println("First Quadrant");
            }else{
                System.out.println("Fourth Quadrant");
            }
        }else{
            if (y > 0){
                System.out.println("Second Quadrant");
            }else{
                System.out.println("Third Quadrant");
            }
        }
        sc.close();
    }
}
