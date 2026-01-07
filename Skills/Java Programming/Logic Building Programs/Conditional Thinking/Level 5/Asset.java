//Take coordinates (x, y) and check if the point lies on the X-axis, Y-axis, or at the origin. 

import java.util.Scanner;

public class Asset{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter abscissa: ");
        int x = sc.nextInt();
        System.out.println("Enter ordinate: ");
        int y = sc.nextInt();

        if (x == 0 && y == 0){
            System.out.println("Origin!");
        } else if(x == 0){
            System.out.println("Y-axis!");
        } else if(y == 0){
            System.out.println("X-axis!");
        }
        sc.close();
    }
}